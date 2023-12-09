from datetime import datetime
from typing import Sequence
from database import Database
from ticket import Ticket
from payment_provider import PaymentProvider


class TicketProvider:
    def __init__(self, database: Database, payment_provider: PaymentProvider):
        self._database: Database = database
        self._payment_provider: PaymentProvider = payment_provider

    def search_ticket(self, client_id: int, date: datetime.date) -> Sequence[Ticket]:
        return list(
            filter(lambda t: t.customer_id == client_id and t.date == date and t.enable, self._database.tickets))

    def buy_ticket(self, client_id: int, date: datetime.date, card_no: str):
        order_id: int = self._database.create_ticket_order()
        amount: float = self._database.get_ticket_amount()
        if self._payment_provider.buy_ticket(order_id, card_no, amount):
            new_ticket = Ticket(client_id, date)
            self._database.add_ticket(new_ticket)
        else:
            raise RuntimeError("Не удалось купить билет")

    def check_tickets(self, qr_code: str):
        for ticket in self._database.tickets:
            if ticket.qr_code == qr_code and ticket.enable:
                ticket.enable = False
                break
        else:
            raise RuntimeError(f"Билет {qr_code} не существует или уже использован")
