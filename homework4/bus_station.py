from ticket_provider import TicketProvider


class BusStation:
    def __init__(self, ticket_provider: TicketProvider):
        self._ticket_provider = ticket_provider

    def check_ticket(self, qr_code: str) -> bool:
        return self._ticket_provider.check_tickets(qr_code)
