from customer import Customer
from database import Database
from customer_provider_interface import ICustomerProvider


class CustomerProvider(ICustomerProvider):
    def __init__(self, database: Database):
        self._database: Database = database

    def registration(self, login: str, password: str):
        for customer in self._database.customers:
            if customer.login == login:
                raise RuntimeError("Пользователь с таким именем существует")

        new_customer = Customer(login, password)
        self._database.add_customer(new_customer)

    def get_customer(self, login: str, password: str) -> Customer:
        for customer in self._database.customers:
            if customer.auth(login, password):
                return customer

        raise RuntimeError("Пользователь не найден или не верный логин или пароль")
