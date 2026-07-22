from pathlib import Path
from src.engine.models import ControlMetrics
from src.engine.loaders.csv_loader import CSVLoader
from .base_provider import BaseMetricsProvider

class ControlProvider(BaseMetricsProvider):

    def calculate(self):

        file = (
            Path(self.data_path)/"control"/"tracking_log.csv")

        df = CSVLoader.load(file)
        print(df.columns)
        print(df.head())

        return ControlMetrics(
            tracking_error=df["tracking_error"].mean(),
            avg_jerk=df["jerk"].mean(),
            stability_score=max(0, 1-df["tracking_error"].mean())
        )