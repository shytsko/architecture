from customer_provider import CustomerProvider
from database import Database
from customer_provider_interface import ICustomerProvider
from payment_provider import PaymentProvider
from ticket_provider import TicketProvider


class Core:
    def __init__(self):
        self._database: Database = Database()
        self._payment_provider: PaymentProvider = PaymentProvider()
        self._customer_provider: ICustomerProvider = CustomerProvider(self._database)
        self._ticket_provider: TicketProvider = TicketProvider(self._database, self._payment_provider)

    @property
    def ticket_provider(self):
        return self._ticket_provider

    @property
    def customer_provider(self):
        return self._customer_provider
