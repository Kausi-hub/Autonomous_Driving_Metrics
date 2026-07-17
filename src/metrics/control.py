import numpy as np


class ControlMetrics:

    @staticmethod
    def path_tracking_error(df):

        return np.mean(
            abs(
                df["target_x"]
                -
                df["actual_x"]
            )
        )

    @staticmethod
    def avg_acceleration(df):

        return df["acceleration"].mean()

    @staticmethod
    def avg_jerk(df):

        return df["jerk"].mean()