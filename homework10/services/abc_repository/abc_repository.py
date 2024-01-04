from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')
T_id = TypeVar('T_id')


class ABCRepository(Generic[T, T_id], ABC):
    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def get_by_id(self, id_: T_id) -> T | None:
        pass

    @abstractmethod
    def create(self, item: T) -> T_id:
        pass

    @abstractmethod
    def update(self, item: T) -> bool:
        pass

    @abstractmethod
    def delete(self, id_: T_id) -> bool:
        pass
