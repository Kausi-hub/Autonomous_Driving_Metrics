import pandas as pd
from pathlib import Path

class CSVLoader:

    @staticmethod
    def load(path):

        file = Path(path)
        if not file.exists(): raise FileNotFoundError(f"Missing data file: {file}")
        return pd.read_csv(file)