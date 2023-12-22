from abc import ABC, abstractmethod
from typing import TypeVar, Iterable, Generic

T = TypeVar("T")
T_id = TypeVar("T_id")


class Editor(Generic[T, T_id], ABC):
    @abstractmethod
    def add(self, item: T) -> bool:
        pass

    @abstractmethod
    def edit(self, item: T) -> bool:
        pass

    @abstractmethod
    def remove(self, item: T) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, id_: T_id) -> T | None:
        pass

    @abstractmethod
    def get_all(self) -> Iterable[T]:
        pass
