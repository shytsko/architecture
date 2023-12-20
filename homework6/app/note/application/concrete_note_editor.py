from datetime import datetime
from typing import Sequence

from .interfaces.note_editor import NoteEditor
from .interfaces.notes_database_context import NotesDatabaseContext
from .interfaces.notes_presenter import NotesPresenter
from ..domain.note import Note


class ConcreteNoteEditor(NoteEditor):
    def __init__(self, db_context: NotesDatabaseContext, notes_presenter: NotesPresenter):
        self._db_context = db_context
        self._notes_presenter = notes_presenter

    def print_all(self):
        self._notes_presenter.print_all(self.get_all())

    def add(self, item: Note) -> bool:
        self._db_context.get_all().append(item)
        return self._db_context.save_changes()

    def edit(self, item: Note) -> bool:
        if item is None:
            return False
        note = self.get_by_id(item.id)
        if note is None:
            return False
        note.title = item.title
        note.details = item.details
        note.user_id = item.user_id
        note.edit_date = datetime.date(datetime.now())
        return self._db_context.save_changes()

    def remove(self, item: Note) -> bool:
        self._db_context.get_all().remove(item)
        return self._db_context.save_changes()

    def get_by_id(self, id_: int) -> Note | None:
        for item in self._db_context.get_all():
            if item.id == id_:
                return item
        return None

    def get_all(self) -> Sequence[Note]:
        return self._db_context.get_all()
