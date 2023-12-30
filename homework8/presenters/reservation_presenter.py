from datetime import datetime
from presenters.model import Model
from presenters.view import View
from presenters.view_observer import ViewObserver


class ReservationPresenter(ViewObserver):

    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view
        self._view.register_observer(self)

    def update_ui_load_tables(self):
        tables = self._model.get_tables()
        self._view.show_tables(tables)

    def on_reservation_table(self, order_date: datetime, table_no: int, client_name: str):
        try:
            reservation_id = self._model.reservation_table(order_date, table_no, client_name)
            self._view.show_reservation_table_result(reservation_id)
        except RuntimeError:
            self._view.show_reservation_table_result(-1)

    def on_change_reservation_table(self, old_reservation: int, new_order_date: datetime, new_table_no: int,
                                    new_client_name: str):
        try:
            self._model.reservation_table_cancellation(old_reservation)
        except RuntimeError:
            self._view.show_reservation_table_result(-1)
        else:
            self.on_reservation_table(new_order_date, new_table_no, new_client_name)
