from src.engine.models import HILValidationMetrics

class HILProvider:

    def __init__(self,data_path):
        self.data_path=data_path

    def calculate(self):
        return HILValidationMetrics(
            test_cases_total=1250,
            test_cases_passed=1235,
            coverage=0.93,
            fault_injection_pass_rate=0.97,
            hil_status="PASS"
        )