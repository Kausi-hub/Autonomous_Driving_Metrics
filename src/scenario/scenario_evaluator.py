from src.engine.models import ScenarioResult

class ScenarioEvaluator:

    SCENARIOS = {
        "Highway Merge": {"min_ttc": 1.5, "max_lane_error": 0.25},
        "Lane Change": {"min_ttc": 1.5, "max_lane_error": 0.20},
        "Pedestrian Crossing": {"min_precision": 0.95, "max_miss_rate": 0.02},
        "Construction Zone": {"max_lane_error": 0.30},
        "Emergency Braking": {"min_ttc": 1.0}
    }

    def evaluate(self, scenario_name: str, metrics: dict) -> ScenarioResult:

        config = self.SCENARIOS[scenario_name]
        failures = []
        if "min_ttc" in config:
            if metrics["min_ttc"] < config["min_ttc"]: failures.append("Unsafe TTC")

        if "max_lane_error" in config:
            if metrics["lane_error"] > config["max_lane_error"]:
                failures.append("High Lane Error")

        if "min_precision" in config:
            if metrics["precision"] < config["min_precision"]:
                failures.append("Poor Detection Precision")

        if "max_miss_rate" in config:
            if metrics["miss_rate"] > config["max_miss_rate"]:
                failures.append("Missed Pedestrian")

        return ScenarioResult(scenario=scenario_name, passed=len(failures)==0, failures=failures)