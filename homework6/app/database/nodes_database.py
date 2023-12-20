from .notes_table import NotesTable
from ..note.infrastructure.persistance.database import Database


class NotesDatabase(Database):
    def __init__(self):
        self._notes_table: NotesTable = NotesTable()

    @property
    def notes_table(self):
        return self._notes_table
