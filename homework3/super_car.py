from car import Car
from car_body_type import CarBodyType
from fuel_type import FuelType
from gearbox_type import GearboxType
from color import Color


class SuperCar(Car):
    def __init__(self, brand: str, model: str, color: Color):
        super().__init__(brand, model, color)
        self._body_type = CarBodyType.SPORT
        self._wheels_count = 3
        self._fuel_type = FuelType.GASOLINE
        self._gearbox_type = GearboxType.AUTOMATIC
        self._engine_volume = 5.0

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
