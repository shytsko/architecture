from abc import ABC, abstractmethod
from fuel_type import FuelType


class Refueling(ABC):

    @abstractmethod
    def fuel(self, fuel_type: FuelType):
        pass
