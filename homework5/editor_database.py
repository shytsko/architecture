import random
from typing import MutableSequence
from homework5.database import Database
from homework5.entity import Entity
from homework5.model_3D import Model3D
from homework5.texture import Texture
from homework5.project_file import ProjectFile


class EditorDatabase(Database):
    def __init__(self, project_file: ProjectFile):
        self._project_file: ProjectFile = project_file
        self._entities: list[Entity] = []
        self.load()

    def load(self):
        models_count = random.randint(5, 10)
        for _ in range(models_count):
            texture_count = random.randint(1, 3)
            textures = [Texture() for _ in range(texture_count)]
            self._entities.extend(textures)
            model = Model3D(textures)
            self._entities.append(model)

    def save(self):
        pass

    def get_all(self) -> MutableSequence[Entity]:
        return self._entities
