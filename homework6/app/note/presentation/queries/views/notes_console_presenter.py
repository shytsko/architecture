from typing import Sequence

from app.note.application.interfaces.notes_presenter import NotesPresenter
from app.note.domain.note import Note


class NotesConsolePresenter(NotesPresenter):
    def print_all(self, notes: Sequence[Note]):
        print(*notes, sep='\n')
