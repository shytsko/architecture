from ticket import Ticket
from typing import Sequence


class Customer:
    _id_generator = iter(range(100, 200))

    def __init__(self, login: str, password: str):
        self._id: int = self._next_id()
        self._thickets: Sequence[Ticket] | None = None
        self._login: str = login
        self._password: str = password

    def _next_id(self):
        return next(self._id_generator)

    @property
    def id(self):
        return self._id

    @property
    def login(self):
        return self._login

    @property
    def thickets(self):
        return self._thickets

    @thickets.setter
    def thickets(self, tickets: Sequence[Ticket]):
        self._thickets = tickets

    def auth(self, login: str, password: str):
        return login == self._login and password == self._password

    def __str__(self):
        return self._login
