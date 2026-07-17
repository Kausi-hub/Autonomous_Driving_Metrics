from pathlib import Path
import pandas as pd


class DatasetLoader:

    def __init__(self, data_path):

        self.data_path = Path(data_path)

    def load_detection_data(self):

        file = self.data_path / "detections.csv"
        print("Loading:", file)

        return pd.read_csv(file)

    def load_planning_data(self):

        file = self.data_path / "planning.csv"

        return pd.read_csv(file)

    def load_control_data(self):

        file = self.data_path / "control.csv"

        return pd.read_csv(file)