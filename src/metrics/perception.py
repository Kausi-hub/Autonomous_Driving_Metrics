import numpy as np


class PerceptionMetrics:

    @staticmethod
    def calculate_precision(df):

        tp = df["tp"].sum()
        fp = df["fp"].sum()
        return tp / (tp + fp)

    @staticmethod
    def calculate_recall(df):

        tp = df["tp"].sum()
        fn = df["fn"].sum()
        return tp / (tp + fn)

    @staticmethod
    def calculate_f1(precision,recall): return (2 * precision * recall /(precision + recall))

    @staticmethod
    def pedestrian_miss_rate(df):

        fn = df["fn"].sum()
        total = (df["tp"].sum() + df["fn"].sum())
        return fn / total