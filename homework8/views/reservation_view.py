from datetime import datetime
from typing import Iterable
from models.entities import Table
from presenters.view import View
from presenters.view_observer import ViewObserver


class ReservationView(View):

    def __init__(self):
        self._observers: list[ViewObserver] = []

    def register_observer(self, observer: ViewObserver):
        self._observers.append(observer)

    def show_tables(self, tables: Iterable[Table]):
        print('--------- Доступные столики ------------')
        for table in tables:
            print(table)
            for reservation in table.reservations:
                print(f'\tЗарезервирован на {reservation.datetime}'
                      f' клиентом {reservation.client}, номер брони {reservation.id}')
        print('----------------------------------------')

    def reservation_table(self, order_date: datetime, table_no: int, client_name: str):
        for observer in self._observers:
            observer.on_reservation_table(order_date, table_no, client_name)

    def change_reservation_table(self, old_reservation: int, new_order_date: datetime, new_table_no: int,
                                 new_client_name: str):
        for observer in self._observers:
            observer.on_change_reservation_table(old_reservation, new_order_date, new_table_no, new_client_name)

    def show_reservation_table_result(self, reservation_id: int):
        if reservation_id > 0:
            print(f'Столик успешно зарегистрирован, номер регистрации {reservation_id}')
        else:
            print('Не удалось зарегистрировать столик')
