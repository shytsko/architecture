from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Сущность
    """

    @property
    @abstractmethod
    def id(self) -> int:
        pass
