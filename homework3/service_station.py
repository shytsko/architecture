from homework3.fuel_type import FuelType
from refueling import Refueling
from wiping import Wiping


class ServiceStation(Refueling, Wiping):
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

    def wip_mirrors(self):
        print("Помыли зеркала")

    def wip_windshield(self):
        print("Помыли лобовое стекло")

    def wip_head_lights(self):
        print("Помыли фары")
