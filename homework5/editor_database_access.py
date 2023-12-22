from typing import Sequence

from homework5.database import Database
from homework5.database_access import DatabaseAccess
from homework5.entity import Entity
from homework5.model_3D import Model3D
from homework5.texture import Texture


class EditorDatabaseAccess(DatabaseAccess):
    def __init__(self, database: Database):
        self._database: Database = database

    def add_entity(self, entity: Entity):
        self._database.get_all().append(entity)

    def remove_entity(self, entity: Entity):
        self._database.get_all().remove(entity)

    def get_all_texture(self) -> Sequence[Texture]:
        return tuple(entity for entity in self._database.get_all() if isinstance(entity, Texture))

    def get_all_model(self) -> Sequence[Model3D]:
        return tuple(entity for entity in self._database.get_all() if isinstance(entity, Model3D))
