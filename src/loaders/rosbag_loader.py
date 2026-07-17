class RosbagLoader:

    def __init__(self, bag_path):
        self.bag_path = bag_path

    def list_topics(self):

        return [
            "/vehicle/odometry",
            "/perception/detections",
            "/planning/trajectory"
        ]

    def load_odometry(self):

        import pandas as pd

        return pd.DataFrame({
            "timestamp":[1,2,3,4,5],
            "x":[0,1,2,3,4],
            "y":[0,0.2,0.4,0.6,0.8],
            "vx":[5.0,5.2,5.1,5.3,5.5]
        })