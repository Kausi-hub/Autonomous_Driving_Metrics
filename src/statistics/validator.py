import numpy as np
import math
import numpy as np
from scipy import stats
from scipy import stats
from scipy.stats import ttest_ind


class StatisticalValidator:

    @staticmethod
    def t_test(
            baseline,
            candidate):

        t_stat, p_value = ttest_ind(
            baseline,
            candidate,
            equal_var=False
        )

        return {
            "t_stat": t_stat,
            "p_value": p_value
        }

    @staticmethod
    def pass_rate(results):

        return (
            sum(results)
            /
            len(results)
        )

    @staticmethod
    def calculate_pass_rate(scenario_results):
        """
        Calculate % scenarios passed
        """

        total = len(scenario_results)

        passed = sum(
            result["passed"]
            for result in scenario_results
        )

        return passed / total

    @staticmethod
    def confidence_interval(values, confidence=0.95):

        values = np.array(values)

        mean = np.mean(values)

        sem = stats.sem(values)

        margin = (
            sem *
            stats.t.ppf(
                (1 + confidence) / 2,
                len(values) - 1
            )
        )

        return {
            "mean": mean,
            "lower": mean - margin,
            "upper": mean + margin
        }
    
    @staticmethod
    def pass_rate_ci(results, confidence=0.95):
            """
            Wilson score confidence interval
            """

            z = 1.96

            n = len(results)

            p = sum(results) / n

            denominator = 1 + (z**2 / n)

            center = (
                p +
                (z**2 / (2*n))
            ) / denominator

            margin = (
                z *
                math.sqrt(
                    (
                        p*(1-p) +
                        z**2/(4*n)
                    ) / n
                )
            ) / denominator

            return {

                "pass_rate": p,

                "lower":
                    max(
                        0,
                        center - margin
                    ),

                "upper":
                    min(
                        1,
                        center + margin
                    )
            }
