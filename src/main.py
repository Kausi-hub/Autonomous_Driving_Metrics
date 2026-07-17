from pathlib import Path
from loaders.dataset_loader import DatasetLoader
from metrics.perception import PerceptionMetrics
from metrics.planning import PlanningMetrics
from metrics.control import ControlMetrics
from stats_utils.validator import StatisticalValidator
from release_gate import ReleaseGate
from database.db_writer import DBWriter
from scenario.scenario_evaluator import ScenarioEvaluator
from scenario.failure_analysis import (top_failure_modes,risk_ranking,release_recommendation)

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

loader = DatasetLoader(PROJECT_ROOT /"data" /"raw")
detection_df = (loader.load_detection_data())
planning_df = (loader.load_planning_data())
control_df = (loader.load_control_data())
precision = (PerceptionMetrics.calculate_precision(detection_df))
recall = (PerceptionMetrics.calculate_recall(detection_df))
f1 = (PerceptionMetrics.calculate_f1(precision,recall))
miss_rate = (PerceptionMetrics.pedestrian_miss_rate(detection_df))
lane_error = (PlanningMetrics.avg_lane_error(planning_df))
min_ttc = (PlanningMetrics.minimum_ttc(planning_df))
collision_count = (PlanningMetrics.collision_risk_events(planning_df))
tracking_error = (ControlMetrics.path_tracking_error(control_df))
avg_accel = (ControlMetrics.avg_acceleration(control_df))
avg_jerk = (ControlMetrics.avg_jerk(control_df))

scenario_engine = ScenarioEvaluator()
# Run all scenarios
scenario_results = []
scenario_results.append(scenario_engine.evaluate("Highway Merge",{"min_ttc": min_ttc,"lane_error": lane_error}))
scenario_results.append(scenario_engine.evaluate("Lane Change",{"min_ttc": min_ttc,"lane_error": lane_error}))
scenario_results.append(scenario_engine.evaluate("Pedestrian Crossing",{"precision": precision,"miss_rate": miss_rate}))
scenario_results.append(scenario_engine.evaluate("Construction Zone",{"lane_error": lane_error}))
scenario_results.append(scenario_engine.evaluate("Emergency Braking",{"min_ttc": min_ttc}))
pass_rate = (StatisticalValidator.calculate_pass_rate(scenario_results))
pass_rate_stats = (StatisticalValidator.pass_rate_ci([result["passed"] for result in scenario_results]))
top_failures = top_failure_modes(scenario_results)
risk_table = risk_ranking(scenario_results)
recommendation = release_recommendation(pass_rate,risk_table)
gate = ReleaseGate()
release = gate.evaluate(
    perception={"precision": precision, "recall": recall},
    planning={"lane_error": lane_error, "min_ttc": min_ttc},
    control={"tracking_error": tracking_error}
)
ttc_ci = (StatisticalValidator.confidence_interval(planning_df["ttc"]))

print("\n")
print("=" * 60)
print("AUTONOMY VALIDATION REPORT")
print("=" * 60)

for result in scenario_results:

    print(f"{result['scenario']} : " f"{'PASS' if result['passed'] else 'FAIL'}")

print("\nPass Rate")
print(f"{pass_rate * 100:.1f}%")
print("\n95% Confidence Interval")
print(f"{pass_rate_stats['lower']*100:.1f}% " f"to " f"{pass_rate_stats['upper']*100:.1f}%")
print("\nTop Failure Modes")
for failure, count in top_failures: print(f"{failure}: {count}")
print("\nRisk Ranking")
for risk in risk_table: print(f"{risk['scenario']} " f"({risk['risk']})")
print("\nRelease Recommendation")
print(recommendation)
print("\nRelease Decision")
print(release)
print("\nTTC Statistics")
print(ttc_ci)

db = DBWriter()
run_id = db.insert_test_run("1.0.0","Highway Merge","Clear")
db.insert_perception_metrics(run_id,precision,recall,f1,miss_rate)
db.insert_planning_metrics(run_id,lane_error,min_ttc,collision_count)
db.insert_control_metrics(run_id,tracking_error,avg_accel,avg_jerk)
db.insert_release_decision(run_id,release["score"],1,release["decision"])
db.close()