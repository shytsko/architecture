from typing import Sequence
from .configuration.note_configuration import NoteConfiguration
from .database import Database
from .db_context import DbContext, ModelBuilder
from ...application.interfaces.notes_database_context import NotesDatabaseContext
from ...domain.note import Note


class DatabaseContext(DbContext, NotesDatabaseContext):
    def __init__(self, database: Database):
        super().__init__(database)
        self._notes = [Note(item.id, item.user_id, item.title, item.details, item.creation_date, item.edit_date)
                       for item in self._database.notes_table.records]

    def get_all(self) -> Sequence[Note]:
        return self._notes

    def _on_model_creating(self, builder: ModelBuilder):
        builder.apply_configuration(NoteConfiguration())
