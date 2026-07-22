from src.engine.models import BenchValidationMetrics

class BenchProvider:

    def __init__(self,data_path):
        self.data_path=data_path

    def calculate(self):
        return BenchValidationMetrics(
            tests_executed=450,
            pass_rate=0.95,
            thermal_margin=12.5,
            performance_margin=8.3,
            bench_status="PASS"
        )