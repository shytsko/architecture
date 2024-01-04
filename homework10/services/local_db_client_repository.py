from services.abc_repository.abc_client_repository import ABCClientRepository
from models.client import Client
import sqlite3
from datetime import date


class LocalDBClientRepository(ABCClientRepository):

    def __init__(self, db_name: str):
        self._db_name = db_name

    def prepare(self):
        with sqlite3.connect(self._db_name) as connection:
            connection.execute('DROP TABLE IF EXISTS clients')
            connection.execute(
                '''
                CREATE TABLE clients(
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                document TEXT,
                surname TEXT,
                firstname TEXT,
                patronymic TEXT,
                birthday DATE)
                ''')
            connection.commit()

    def get_all(self) -> list[Client]:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('SELECT * FROM clients').fetchall()
            return [Client(client_id=row[0],
                           document=row[1],
                           sur_name=row[2],
                           first_name=row[3],
                           patronymic=row[4],
                           birthday=date.fromisoformat(row[5]))
                    for row in res]

    def get_by_id(self, id_: int) -> Client | None:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute('SELECT * FROM clients WHERE client_id = ?', (id_,)).fetchone()
            return Client(client_id=res[0],
                          document=res[1],
                          sur_name=res[2],
                          first_name=res[3],
                          patronymic=res[4],
                          birthday=date.fromisoformat(res[5])) \
                if res else None

    def create(self, item: Client) -> int:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('INSERT INTO clients(document, surname, firstname, patronymic, birthday)'
                                     ' VALUES (?, ?, ?, ?, ?)',
                                     (item.document, item.sur_name, item.first_name, item.patronymic,
                                      item.birthday))
            connection.commit()
            return res.lastrowid

    def update(self, item: Client) -> bool:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute(
                '''
                    UPDATE clients
                    SET document = ?, firstname = ?, surname = ?, patronymic = ?, birthday = ?
                    WHERE client_id = ?
                    ''',
                (item.document, item.first_name, item.sur_name,
                 item.patronymic, item.birthday, item.client_id)
            ).rowcount
            return res > 0

    def delete(self, id_: int) -> bool:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('DELETE FROM clients WHERE client_id = ?', (id_,)).rowcount
            return res > 0
