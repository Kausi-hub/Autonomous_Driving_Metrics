from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class BaseMetricsProvider(ABC, Generic[T]):

    def __init__(self, data_path):

        self.data_path = data_path

    @abstractmethod
    def calculate(self) -> T:
        """
        Calculate domain metrics.
        """
        raise NotImplementedError