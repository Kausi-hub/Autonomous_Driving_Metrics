from collections import Counter


def top_failure_modes(scenario_results):

    failures = []

    for result in scenario_results:

        failures.extend(
            result["failures"]
        )

    return Counter(
        failures
    ).most_common()

def risk_ranking(scenario_results):

    ranking = []

    for result in scenario_results:

        if result["passed"]:

            risk = "LOW"

        elif len(result["failures"]) == 1:

            risk = "MEDIUM"

        else:

            risk = "HIGH"

        ranking.append({

            "scenario":
                result["scenario"],

            "risk":
                risk,

            "failures":
                result["failures"]
        })

    return sorted(

        ranking,

        key=lambda x: (
            0 if x["risk"] == "HIGH"
            else 1 if x["risk"] == "MEDIUM"
            else 2
        )
    )

def release_recommendation(
        pass_rate,
        risk_table):

    high_risk = sum(

        1

        for item

        in risk_table

        if item["risk"] == "HIGH"
    )

    if pass_rate >= 0.95 and high_risk == 0:

        return "PASS"

    if pass_rate >= 0.80 and high_risk <= 1:

        return "CONDITIONAL PASS"

    return "FAIL"