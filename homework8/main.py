from datetime import datetime, timedelta

from models.table_service import TableService
from presenters.reservation_presenter import ReservationPresenter
from views.reservation_view import ReservationView

if __name__ == '__main__':
    table_service = TableService()
    reservation_view = ReservationView()
    reservation_presenter = ReservationPresenter(table_service, reservation_view)
    reservation_presenter.update_ui_load_tables()
    reservation_view.reservation_table(datetime.now(), 3, 'client1')
    reservation_view.reservation_table(datetime.now(), 8, 'client2')
    reservation_view.reservation_table(datetime.now(), 4, 'client3')
    reservation_view.reservation_table(datetime.now(), 3, 'client4')
    reservation_presenter.update_ui_load_tables()

    reservation_view.change_reservation_table(1001, datetime.now() + timedelta(days=3), 5, 'new_client')
    reservation_presenter.update_ui_load_tables()
