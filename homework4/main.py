from datetime import datetime

from core import Core
from mobile_app import MobileApp
from bus_station import BusStation

if __name__ == '__main__':
    core = Core()

    app: MobileApp = MobileApp(core.customer_provider, core.ticket_provider)
    bus_station: BusStation = BusStation(core.ticket_provider)

    app.login('customer1', 'password1')
    app.search_ticket(datetime.date(datetime.now()))
    tickets = app.get_tickets()
    print(*tickets)

    app.buy_ticket('0000000000000001', datetime.date(datetime.now()))
    app.search_ticket(datetime.date(datetime.now()))
    tickets = app.get_tickets()
    print(*tickets)

    bus_station.check_ticket(tickets[0].qr_code)
    not_valid_ticket = tickets[0]
    app.search_ticket(datetime.date(datetime.now()))
    tickets = app.get_tickets()
    print(*tickets)

    try:
        bus_station.check_ticket(not_valid_ticket.qr_code)
    except RuntimeError as e:
        print(e)

