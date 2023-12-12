# 1. Спроектировать абстрактный класс «Car» у которого должны быть свойства: марка, модель, цвет, тип кузова,
# число колёс, тип топлива, тип коробки передач, объём двигателя; методы: движение, обслуживание, переключение передач,
# включение фар, включение дворников.
# 2. Создать конкретный автомобиль путём наследования класса «Car».
# 3. Расширить абстрактный класс «Car», добавить метод: подметать улицу. Создать конкретный автомобиль путём
# наследования класса «Car». Провести проверку принципа SRP.
# 4. Расширить абстрактный класс «Car», добавить метод: включение противотуманных фар, перевозка груза. Провести
# проверку принципа OCP.
# 5. Создать конкретный автомобиль путём наследования класса «Car», определить число колёс = 3. Провести проверку
# принципа LSP.
# 6. Создать интерфейс «Заправочная станция», создать метод: заправка топливом.
# 7. Имплементировать метод интерфейса «Заправочная станция» в конкретный класс «Car».
# 8. Добавить в интерфейс «Заправочная станция» методы: протирка лобового стекла, протирка фар, протирка зеркал.
# 9. Имплементировать все методы интерфейса «Заправочная станция» в конкретный класс «Car». Провести проверку
# принципа ISP. Создать дополнительный/е интерфейсы и имплементировать их в конкретный класс «Car». Провести
# проверку принципа ISP.
# 10. Создать путём наследования класса «Car» два автомобиля: с бензиновым и дизельным двигателями, имплементировать
# метод «Заправка топливом» интерфейса «Заправочная станция». Реализовать заправку каждого автомобиля подходящим
# топливом. Провести проверку принципа DIP.
#  TODO: Домашнее задание:
#      * Доработать приложение, спроектированное на семинаре. Добавить тип, описывающий "автомойку" и "сервисную станцию".
#      * Продемонстрировать работу получившейся программы,
#      * создать несколько типов автомобилей,
#      * загнать каждый автомобиль на заправку, а затем и на автомойку.


from abc import ABC, abstractmethod

from car_body_type import CarBodyType
from fuel_type import FuelType
from gearbox_type import GearboxType
from color import Color
from homework3.wiping import Wiping
from refueling import Refueling


class Car(ABC):
    def __init__(self, brand: str, model: str, color: Color):
        self._brand: str = brand
        self._model: str = model
        self._color: Color = color
        self._body_type: CarBodyType | None = None
        self._wheels_count: int = 0
        self._fuel_type: FuelType | None = None
        self._gearbox_type: GearboxType | None = None
        self._engine_volume: float = 0.0
        self._fog_lights: bool = False
        self._refueling: Refueling | None = None
        self._wiping: Wiping | None = None

    @abstractmethod
    def movement(self) -> None:
        pass

    @abstractmethod
    def maintenance(self) -> None:
        pass

    @abstractmethod
    def gear_shifting(self) -> bool:
        pass

    @abstractmethod
    def switch_headlights(self) -> bool:
        pass

    @abstractmethod
    def switch_wipers(self) -> bool:
        pass

    def switch_fog_lights(self):
        self._fog_lights = not self._fog_lights
        return self._fog_lights

    @property
    def wheels_count(self):
        return self._wheels_count

    @property
    def fuel(self):
        return self._fuel_type

    def go_to_refueling(self, refueling_station: Refueling):
        self._refueling = refueling_station
        print(f"Автомобиль {self} заехал на заправочную станцию {self._refueling}")

    def refuel(self):
        if self._refueling:
            self._refueling.fuel(self._fuel_type)

    def leave_refueling(self):
        print(f"Автомобиль {self} уехал с заправочной станции {self._refueling}")
        self._refueling = None

    def go_to_washing(self, washing_station: Wiping):
        self._wiping = washing_station
        print(f"Автомобиль {self} заехал на мойку {self._wiping}")

    def washing(self):
        if self._wiping:
            self._wiping.wip_mirrors()
            self._wiping.wip_windshield()
            self._wiping.wip_head_lights()

    def leave_washing(self):
        print(f"Автомобиль {self} уехал с мойки {self._wiping}")
        self._wiping = None

    def __str__(self):
        return f"{self._brand} {self._model}"
