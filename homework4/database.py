from datetime import datetime
from random import randint

from ticket import Ticket
from customer import Customer


class Database:
    __generate_id = 100

    def __init__(self):
        self._tickets: list[Ticket] = []
        self._customers: list[Customer] = []

        for i in range(1, 6):
            self.add_customer(Customer(f'customer{i}', f'password{i}'))
        for i in range(10):
            self.add_ticket(Ticket(randint(100, 105), datetime.date(datetime.now())))

    def add_customer(self, customer: Customer):
        self._customers.append(customer)

    def add_ticket(self, ticket: Ticket):
        self._tickets.append(ticket)

    @property
    def tickets(self):
        return self._tickets

    @property
    def customers(self):
        return self._customers

    def get_ticket_amount(self) -> float:
        return 45.0

    @classmethod
    def create_ticket_order(cls):
        cls.__generate_id += 1
        return cls.__generate_id
