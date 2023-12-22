from abc import ABC, abstractmethod
from typing import MutableSequence

from app.note.domain.note import Note


class NotesDatabaseContext(ABC):
    @abstractmethod
    def get_all(self) -> MutableSequence[Note]:
        pass

    @abstractmethod
    def save_changes(self) -> bool:
        pass
