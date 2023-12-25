from abc import ABC, abstractmethod
from typing import Iterable

from models.entities import Table
from presenters.view_observer import ViewObserver


class View(ABC):

    @abstractmethod
    def show_tables(self, tables: Iterable[Table]):
        pass

    @abstractmethod
    def show_reservation_table_result(self, reservation_id: int):
        pass

    @abstractmethod
    def register_observer(self, observer: ViewObserver):
        pass
