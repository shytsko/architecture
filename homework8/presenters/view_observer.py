from abc import ABC, abstractmethod
from datetime import datetime


class ViewObserver(ABC):
    @abstractmethod
    def on_reservation_table(self, order_date: datetime, table_no: int, client_name: str):
        pass

    @abstractmethod
    def on_change_reservation_table(self, old_reservation: int, new_order_date: datetime, new_table_no: int,
                                    new_client_name: str):
        pass
