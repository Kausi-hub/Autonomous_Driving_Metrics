from statistics.validator import StatisticalValidator
from collections import Counter


class ScenarioEvaluator:

    SCENARIOS = {
        "Highway Merge": {"min_ttc": 1.5,"max_lane_error": 0.25},
        "Lane Change": {"min_ttc": 1.5,"max_lane_error": 0.20},
        "Pedestrian Crossing": {"min_precision": 0.95,"max_miss_rate": 0.02},
        "Construction Zone": {"max_lane_error": 0.30},
        "Emergency Braking": {"min_ttc": 1.0}
    }

    def evaluate(self,scenario_name,metrics):

        cfg = self.SCENARIOS[scenario_name]
        failures = []
        passed = True
        if "min_ttc" in cfg:
            if metrics["min_ttc"] < cfg["min_ttc"]:
                failures.append("Unsafe TTC")
                passed = False
        if "max_lane_error" in cfg:
            if (metrics["lane_error"] > cfg["max_lane_error"]):
                failures.append("High Lane Error")
                passed = False
        if "min_precision" in cfg:
            if (metrics["precision"] < cfg["min_precision"]):
                failures.append("Poor Detection Precision")
                passed = False
        if "max_miss_rate" in cfg:
            if (metrics["miss_rate"] > cfg["max_miss_rate"]):
                failures.append("Missed Pedestrian")
                passed = False
        return {"scenario": scenario_name,"passed": passed,"failures": failures}

def risk_ranking(results):

    ranking = []
    for result in results:
        if not result["passed"]:
            severity = "HIGH"
        else:
            severity = "LOW"
        ranking.append({"scenario": result["scenario"],"risk": severity})
    return sorted(ranking,key=lambda x: 0 if x["risk"] == "HIGH" else 1)


def top_failure_modes(results):

    failures = []
    for result in results:
        failures.extend(result["failures"])
    return Counter(failures).most_common(10)