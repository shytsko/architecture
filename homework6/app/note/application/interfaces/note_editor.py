from abc import ABC, abstractmethod

from .editor import Editor
from ...domain.note import Note


class NoteEditor(Editor[Note, int], ABC):
    @abstractmethod
    def print_all(self):
        pass
