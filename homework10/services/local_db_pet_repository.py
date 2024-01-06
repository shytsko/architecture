from services.abc_repository.abc_pet_repository import ABCPetRepository
from models.pet import Pet
import sqlite3
from datetime import date


class LocalDBCPetRepository(ABCPetRepository):

    def __init__(self, db_name: str):
        self._db_name = db_name

    def prepare(self):
        with sqlite3.connect(self._db_name) as connection:
            connection.execute('DROP TABLE IF EXISTS pets')
            connection.execute(
                '''
                CREATE TABLE pets(
                pet_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                name TEXT,
                birthday DATE)
                ''')
            connection.commit()

    def get_all(self) -> list[Pet]:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('SELECT * FROM pets').fetchall()
            return [Pet(pet_id=row[0],
                        client_id=row[1],
                        name=row[2],
                        birthday=date.fromisoformat(row[3]))
                    for row in res]

    def get_by_id(self, id_: int) -> Pet | None:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute('SELECT * FROM pets WHERE pet_id = ?', (id_,)).fetchone()
            return Pet(pet_id=res[0],
                       client_id=res[1],
                       name=res[2],
                       birthday=date.fromisoformat(res[3])) \
                if res else None

    def create(self, item: Pet) -> int:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('INSERT INTO pets(client_id, name, birthday)'
                                     ' VALUES (?, ?, ?)',
                                     (item.client_id, item.name, item.birthday))
            connection.commit()
            return res.lastrowid

    def update(self, item: Pet) -> bool:
        with (sqlite3.connect(self._db_name) as connection):
            res = connection.execute(
                '''
                    UPDATE pets
                    SET client_id = ?, name = ?, birthday = ?
                    WHERE pet_id = ?
                    ''',
                (item.client_id, item.name, item.birthday, item.pet_id)
            ).rowcount
            return res > 0

    def delete(self, id_: int) -> bool:
        with sqlite3.connect(self._db_name) as connection:
            res = connection.execute('DELETE FROM pets WHERE pet_id = ?', (id_,)).rowcount
            return res > 0
