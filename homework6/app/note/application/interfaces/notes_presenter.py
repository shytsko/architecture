from abc import ABC, abstractmethod
from typing import Sequence

from app.note.domain.note import Note


class NotesPresenter(ABC):
    @abstractmethod
    def print_all(self, notes: Sequence[Note]):
        pass
