from abc import ABC, abstractmethod
from typing import Sequence
from datetime import datetime
from models.entities import Table


class Model(ABC):
    @abstractmethod
    def get_tables(self) -> Sequence[Table]:
        pass

    @abstractmethod
    def reservation_table(self, reservation_datetime: datetime, table_no: int, client_name: str) -> int:
        pass

    @abstractmethod
    def reservation_table_cancellation(self, reservation_id: int):
        pass
