from app.note.application.interfaces.note_editor import NoteEditor
from app.note.domain.note import Note
from .controller import Controller


class NotesController(Controller):
    def __init__(self, notes_editor: NoteEditor):
        self._notes_editor = notes_editor

    def route_add_note(self, note: Note):
        self._notes_editor.add(note)

    def route_remove_note(self, note: Note):
        self._notes_editor.remove(note)

    def route_get_all(self):
        self._notes_editor.print_all()
