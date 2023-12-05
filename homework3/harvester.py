from car import Car
from car_body_type import CarBodyType
from fuel_type import FuelType
from gearbox_type import GearboxType
from color import Color


class Harvester(Car):
    def __init__(self, brand: str, model: str, color: Color):
        super().__init__(brand, model, color)
        self._body_type = CarBodyType.PICKUP
        self._wheels_count = 4
        self._fuel_type = FuelType.DIESEL
        self._gearbox_type = GearboxType.MANUAL
        self._engine_volume = 4.0

    def movement(self) -> None:
        pass

    def maintenance(self) -> None:
        pass

    def gear_shifting(self) -> bool:
        pass

    def switch_headlights(self) -> bool:
        pass

    def switch_wipers(self) -> bool:
        pass

    def sweeping(self):
        print("Подметаем улицу")