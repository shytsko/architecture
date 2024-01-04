from services.abc_repository.abc_consultation_repository import ABCConsultationRepository
from models.consultation import Consultation
import sqlite3
from datetime import datetime


class LocalDBCConsultationRepository(ABCConsultationRepository):

    def __init__(self, db_name: str):
        self._db_name = db_name

    def prepare(self):
        with sqlite3.connect(self._db_name) as connection:
            connection.execute('DROP TABLE IF EXISTS consultations')
            connection.execute(
                '''
                CREATE TABLE consultations(
                consultation_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                pet_id INTEGER,
                consultation_date DATETIME,
                description TEXT)             
                ''')
            connection.commit()

    def get_all(self) -> list[Consultation]:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('SELECT * FROM consultations').fetchall()
            return [Consultation(consultation_id=row[0],
                                 client_id=row[1],
                                 pet_id=row[2],
                                 date_time=datetime.fromisoformat(row[3]),
                                 description=row[4])
                    for row in res]

    def get_by_id(self, id_: int) -> Consultation | None:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute('SELECT * FROM consultations WHERE consultation_id = ?', (id_,)).fetchone()
            return Consultation(consultation_id=res[0],
                                client_id=res[1],
                                pet_id=res[2],
                                date_time=datetime.fromisoformat(res[3]),
                                description=res[4]) \
                if res else None

    def create(self, item: Consultation) -> int:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('INSERT INTO consultations(client_id, pet_id, consultation_date, description)'
                                     ' VALUES (?, ?, ?, ?)',
                                     (item.client_id, item.pet_id, item.date_time, item.description))
            connection.commit()
            return res.lastrowid

    def update(self, item: Consultation) -> bool:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute(
                '''
                    UPDATE consultations
                    SET client_id = ?, pet_id = ?, consultation_date = ?, description = ?
                    WHERE consultation_id = ?
                    ''',
                (item.client_id, item.pet_id, item.date_time, item.description, item.consultation_id)
            ).rowcount
            return res > 0

    def delete(self, id_: int) -> bool:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('DELETE FROM consultations WHERE consultation_id = ?', (id_,)).rowcount
            return res > 0
