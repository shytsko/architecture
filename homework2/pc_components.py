class PCComponent:

    def __init__(self, name: str, warranty: int, price: float):
        self._name = name
        self._warranty = warranty
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def warranty(self) -> int:
        return self._warranty

    @property
    def price(self) -> float:
        return self._price

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"


class Case(PCComponent):
    pass


class PowerSupply(PCComponent):
    pass


class MotherBoard(PCComponent):
    pass


class CPU(PCComponent):
    pass


class RAM(PCComponent):
    pass


class Storage(PCComponent):
    pass


class GPU(PCComponent):
    pass
