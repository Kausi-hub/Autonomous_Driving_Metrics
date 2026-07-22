from collections import Counter
from src.engine.models import (FailureMode, RiskItem, ScenarioResult, FailureAnalysisResult)

class FailureAnalyzer:

    def top_failure_modes(self, results:list[ScenarioResult]):

        failures=[]
        for result in results: failures.extend(result.failures)
        counts = Counter(failures)
        return [FailureMode(failure=name, count=count) for name,count in counts.most_common(10)]

    def risk_ranking(self, results:list[ScenarioResult]):

        ranking=[]
        for result in results:
            if result.passed: risk="LOW"
            elif len(result.failures)==1: risk="MEDIUM"
            else: risk="HIGH"
            ranking.append(RiskItem(scenario=result.scenario, risk=risk, failures=result.failures))

        priority = {"HIGH":0, "MEDIUM":1, "LOW":2}
        return sorted(ranking, key=lambda x: priority[x.risk])

    def release_recommendation(self, pass_rate:float, risks:list[RiskItem]):

        high_risk=sum(1 for item in risks if item.risk=="HIGH")
        if pass_rate >=0.95 and high_risk==0: return "PASS"
        if pass_rate>=0.80 and high_risk<=1:  return "CONDITIONAL PASS"
        return "FAIL"

    def analyze(self, results, pass_rate):

        risks=self.risk_ranking(results)
        return FailureAnalysisResult(

            top_failures= self.top_failure_modes(results),
            risk_ranking= risks,
            recommendation= self.release_recommendation(pass_rate, risks))