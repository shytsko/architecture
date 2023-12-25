from datetime import datetime


class Table:
    _no_generator = iter(range(1, 1000))

    def __init__(self):
        self._no: int = self._next_no()
        self._reservations: list[Reservation] = []

    @property
    def no(self):
        return self._no

    @property
    def reservations(self):
        return self._reservations

    def __str__(self):
        return f'Столик №{self._no}'

    def _next_no(self):
        return next(self._no_generator)


class Reservation:
    _id_generator = iter(range(1001, 10000))

    def __init__(self, table: Table, client_name: str, datetime_: datetime):
        self._id = self._next_id()
        self._table = table
        self._client = client_name
        self._datetime = datetime_

    @property
    def id(self):
        return self._id

    def table(self):
        return self._table

    def client(self):
        return self._client

    def datetime(self):
        return self._datetime

    def _next_id(self):
        return next(self._id_generator)
