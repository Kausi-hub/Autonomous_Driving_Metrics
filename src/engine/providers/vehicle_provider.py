from src.engine.models import VehicleValidationMetrics

class VehicleProvider:

    def __init__(self,data_path): self.data_path=data_path

    def calculate(self):

        return VehicleValidationMetrics(
            miles_completed=12500,
            disengagement_rate=0.002,
            safety_events=1,
            vehicle_status="CONDITIONAL"
        )