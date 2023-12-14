from abc import ABC, abstractmethod
from typing import MutableSequence

from homework5.entity import Entity


class Database(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_all(self) -> MutableSequence[Entity]:
        pass
