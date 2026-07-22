from src.engine.models import ReleaseReadinessModel
from src.engine.providers.perception_provider import PerceptionProvider
from src.engine.providers.planning_provider import PlanningProvider
from src.engine.providers.control_provider import ControlProvider
from src.engine.providers.software_provider import SoftwareProvider
from src.engine.providers.hil_provider import HILProvider
from src.engine.providers.bench_provider import BenchProvider
from src.engine.providers.vehicle_provider import VehicleProvider
from src.engine.providers.statistics_provider import StatisticsProvider
from src.engine.providers.release_provider import ReleaseProvider
from src.scenario.scenario_evaluator import ScenarioEvaluator
from src.scenario.failure_analysis import FailureAnalyzer


class MetricsEngine:

    def __init__(self,data_path):

        self.data_path=data_path
        self.perception = (PerceptionProvider(data_path))
        self.planning = (PlanningProvider(data_path))
        self.control = (ControlProvider(data_path))
        self.software = (SoftwareProvider(data_path))
        self.hil = (HILProvider(data_path))
        self.bench = (BenchProvider(data_path))
        self.vehicle = (VehicleProvider(data_path))
        self.statistics = (StatisticsProvider())
        self.release = (ReleaseProvider())
        self.scenario_evaluator = ScenarioEvaluator()
        self.failure_analyzer = FailureAnalyzer()

    def run(self):

            perception = (self.perception.calculate())
            planning = (self.planning.calculate())
            control = (self.control.calculate())
            software = (self.software.calculate())
            hil = (self.hil.calculate())
            bench = (self.bench.calculate())
            vehicle = (self.vehicle.calculate())
            statistics = (self.statistics.calculate([perception, planning, control, software, hil, bench, vehicle]))
            release = (self.release.calculate(statistics))
            scenario_results = []
            scenario_metrics = {
                "Highway Merge": {"min_ttc": planning.min_ttc, "lane_error": planning.lane_error},
                "Lane Change": {"min_ttc": planning.min_ttc, "lane_error": planning.lane_error},
                "Pedestrian Crossing": {"precision": perception.precision, "miss_rate": perception.miss_rate},
                "Construction Zone": {"lane_error": planning.lane_error},
                "Emergency Braking": {"min_ttc": planning.min_ttc}
            }

            for scenario, metrics in scenario_metrics.items():
                scenario_results.append(self.scenario_evaluator.evaluate(scenario, metrics))

            failure_analysis = (self.failure_analyzer.analyze(scenario_results, statistics.pass_rate))

            return ReleaseReadinessModel(perception=perception, planning=planning, control=control,
                    software=software, hil=hil, bench=bench, vehicle=vehicle, statistics=statistics,
                    release=release, failure_analysis=failure_analysis,)                