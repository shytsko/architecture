from datetime import datetime


class Ticket:
    _id_generator = iter(range(1000, 2000))

    def __init__(self, customer_id: int, date: datetime.date):
        self._id: int = self._next_id()
        self._customer_id: int = customer_id
        self._date: datetime.date = date
        self._enable: bool = True
        self._qr_code: str = f"ticket{self._id}"

    def _next_id(self):
        return next(self._id_generator)


    @property
    def id(self):
        return self._id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def date(self):
        return self._date

    @property
    def qr_code(self):
        return self._qr_code

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    def __str__(self):
        return self._qr_code
