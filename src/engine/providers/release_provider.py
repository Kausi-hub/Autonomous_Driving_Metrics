from src.engine.models import (ReleaseMetrics, ReleaseDecision)

class ReleaseProvider:

    def calculate(self, statistics):

        score = (statistics.pass_rate * 100)
        decision = (ReleaseDecision.PASS if score > 90 else ReleaseDecision.CONDITIONAL)
        return ReleaseMetrics(score=score, decision=decision)