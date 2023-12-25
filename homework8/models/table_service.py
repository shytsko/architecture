from datetime import datetime
from typing import Sequence
from models.entities import Reservation, Table
from presenters.model import Model


class TableService(Model):

    def __init__(self):
        tables = [Table() for _ in range(5)]
        self._tables: dict[int, Table] = {table.no: table for table in tables}
        self._reservations: dict[int, Reservation] = {}

    def get_tables(self) -> Sequence[Table]:
        return tuple(self._tables.values())

    def reservation_table(self, reservation_datetime: datetime, table_no: int, client_name: str) -> int:
        table = self._tables.get(table_no)
        if table is not None:
            reservation = Reservation(table, client_name, reservation_datetime)
            self._reservations[reservation.id] = reservation
            table.reservations.append(reservation)
            return reservation.id
        else:
            raise RuntimeError('Ошибка бронирования (некорректный номер столика)')

    def reservation_table_cancellation(self, reservation_id: int):
        reservation = self._reservations.get(reservation_id)
        if reservation is not None:
            reservation.table().reservations.remove(reservation)
            self._reservations.pop(reservation_id)
        else:
            raise RuntimeError('Ошибка отмены бронирования (некорректный номер бронирования)')
