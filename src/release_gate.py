class ReleaseGate:

    def evaluate(self,perception,planning,control):

        score = 100
        findings = []
        if perception["precision"] < 0.95:
            score -= 15
            findings.append("Detection precision below threshold")

        if perception["recall"] < 0.95:
            score -= 15
            findings.append("Detection recall below threshold")

        if planning["min_ttc"] < 1.5:
            score -= 25
            findings.append("Unsafe TTC event detected")

        if planning["lane_error"] > 0.25:
            score -= 15
            findings.append("Lane error exceeded threshold")

        if control["tracking_error"] > 0.10:
            score -= 15
            findings.append("Tracking error exceeded threshold")

        decision = ("PASS" if score >= 80 else "FAIL")
        risk = self.compute_risk(score)
        return {"score": score,"risk": risk,"decision": decision,"findings": findings}

    @staticmethod
    def compute_risk(score):

        if score >= 90: return "LOW"
        elif score >= 80: return "MEDIUM"
        return "HIGH"