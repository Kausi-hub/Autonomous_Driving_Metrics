class PlanningMetrics:

    @staticmethod
    def avg_lane_error(df):

        return df["lane_error"].mean()

    @staticmethod
    def minimum_ttc(df):

        return df["ttc"].min()

    @staticmethod
    def collision_risk_events(
        df,
        threshold=1.0
    ):

        return len(
            df[df["ttc"] < threshold]
        )