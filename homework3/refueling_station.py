from fuel_type import FuelType
from refueling import Refueling


class RefuelingStation(Refueling):
    def fuel(self, fuel_type: FuelType):
        match fuel_type:
            case FuelType.DIESEL:
                print("Заправка дизельным топливом")
            case FuelType.DIESEL:
                print("Заправка бензином")
