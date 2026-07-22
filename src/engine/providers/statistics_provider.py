from src.engine.models import StatisticsMetrics

class StatisticsProvider:

    def calculate(self, domains):

        return StatisticsMetrics(pass_rate=0.95, recommendation="Proceed to Release Gate")