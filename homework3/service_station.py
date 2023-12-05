from homework3.fuel_type import FuelType
from refueling import Refueling
from wiping import Wiping


class ServiceStation(Refueling, Wiping):

    def fuel(self, fuel_type: FuelType):
        match fuel_type:
            case FuelType.DIESEL:
                print("Заправка дизельным топливом")
            case FuelType.DIESEL:
                print("Заправка бензином")

    def wip_mirrors(self):
        print("Помыли зеркала")

    def wip_windshield(self):
        print("Помыли ветровое стекло")

    def wip_head_lights(self):
        print("Помыли фары")
