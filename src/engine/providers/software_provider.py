from pathlib import Path
from src.engine.models import SoftwareIntegrationMetrics
from src.engine.loaders.csv_loader import CSVLoader

class SoftwareProvider:

    def __init__(self,data_path): self.data_path=data_path

    def calculate(self):

        df = CSVLoader.load(Path(self.data_path)/"software"/"test_results.csv")
        total=len(df)
        passed=sum(df["status"]=="PASS")

        return SoftwareIntegrationMetrics(
            build_success_rate=passed/total,
            unit_test_pass_rate=passed/total,
            static_analysis_score=100-df["defects"].sum(),
            defect_density=df["defects"].mean(),
            integration_status="PASS" if passed==total else "FAIL"
        )