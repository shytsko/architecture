from fuel_type import FuelType
from refueling import Refueling


class RefuelingStation(Refueling):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def fuel(self, fuel_type: FuelType):
        match fuel_type:
            case FuelType.DIESEL:
                print("Заправка дизельным топливом")
            case FuelType.GASOLINE:
                print("Заправка бензином")
