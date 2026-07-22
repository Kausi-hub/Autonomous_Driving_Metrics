from pathlib import Path
from src.engine.models import PlanningMetrics
from src.engine.loaders.csv_loader import CSVLoader
from .base_provider import BaseMetricsProvider

class PlanningProvider(BaseMetricsProvider):

    def calculate(self):
        file = (Path(self.data_path)/"planning"/"trajectory_error.csv")
        df = CSVLoader.load(file)
        return PlanningMetrics(lane_error=df["lane_error"].mean(), min_ttc=df["ttc"].min(),
            comfort_score=max( 0, 1-df["lane_error"].mean())
        )