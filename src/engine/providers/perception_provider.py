from pathlib import Path
from sklearn.metrics import (precision_score, recall_score, f1_score)
from src.engine.models import PerceptionMetrics
from src.engine.loaders.csv_loader import CSVLoader
from .base_provider import BaseMetricsProvider

class PerceptionProvider(BaseMetricsProvider):

    def calculate(self):
        file = (Path(self.data_path)/"perception"/"detection_results.csv")
        df = CSVLoader.load(file)
        precision = float(precision_score(df["actual"], df["detected"], average="weighted"))
        recall = float(recall_score(df["actual"], df["detected"], average="weighted"))
        f1 = float(f1_score(df["actual"], df["detected"], average="weighted"))
        miss_rate = 1 - recall
        return PerceptionMetrics(precision=precision, recall=recall, f1=f1, miss_rate=miss_rate)