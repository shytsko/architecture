import datetime

from customer import Customer
from homework4.customer_provider_interface import ICustomerProvider
from ticket_provider import TicketProvider
from ticket import Ticket
from typing import Sequence


class MobileApp:

    def __init__(self, customer_provider: ICustomerProvider, ticket_provider: TicketProvider):
        self._ticket_provider: TicketProvider = ticket_provider
        self._customer_provider: ICustomerProvider = customer_provider
        self._customer: Customer | None = None

    def login(self, login: str, password: str):
        self._customer = self._customer_provider.get_customer(login, password)
        if self._customer is None:
            raise RuntimeError("Вход не выполнен")

    def get_tickets(self) -> Sequence[Ticket]:
        return self._customer.thickets

    def search_ticket(self, date: datetime.date):
        self._customer.thickets = self._ticket_provider.search_ticket(self._customer.id, date)

    def buy_ticket(self, card_no: str, date: datetime.date) -> bool:
        return self._ticket_provider.buy_ticket(self._customer.id, date, card_no)

