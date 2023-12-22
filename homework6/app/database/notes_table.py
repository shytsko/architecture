from .note_record import NoteRecord


class NotesTable:
    def __init__(self):
        self._records: list[NoteRecord] = []
        self._prepare_record()

    def _prepare_record(self):
        self._records.extend(NoteRecord(f"Note {i}", f"Detail {i}") for i in range(10))

    @property
    def records(self):
        return self._records
