from app.database.nodes_database import NotesDatabase
from app.note.application.concrete_note_editor import ConcreteNoteEditor
from app.note.domain.note import Note
from app.note.infrastructure.persistance.database_context import DatabaseContext
from app.note.presentation.queries.controllers.notes_controller import NotesController
from app.note.presentation.queries.views.notes_console_presenter import NotesConsolePresenter

if __name__ == '__main__':
    notes_editor = ConcreteNoteEditor(DatabaseContext(NotesDatabase()), NotesConsolePresenter())
    notes_controller = NotesController(notes_editor)
    notes_controller.route_get_all()
    print('----------------------')

    new_note = Note(1500, 20002, "new note", "new note detail", None, None)

    notes_controller.route_add_note(new_note)
    notes_controller.route_get_all()
    print('----------------------')


    notes_controller.route_remove_note(new_note)
    notes_controller.route_get_all()
