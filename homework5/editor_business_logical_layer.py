import random
import time

from homework5.business_logical_layer import BusinessLogicalLayer
from typing import Sequence

from homework5.database_access import DatabaseAccess
from homework5.model_3D import Model3D
from homework5.texture import Texture


class EditorBusinessLogicalLayer(BusinessLogicalLayer):
    def __init__(self, database_access: DatabaseAccess):
        self._database_access: DatabaseAccess = database_access

    def get_all_models(self) -> Sequence[Model3D]:
        return self._database_access.get_all_model()

    def get_all_textures(self) -> Sequence[Texture]:
        return self._database_access.get_all_texture()

    def render_model(self, model: Model3D):
        self._process_render(model)

    def render_all(self):
        for model in self.get_all_models():
            self._process_render(model)

    def _process_render(self, model: Model3D):
        time.sleep(2.5 - random.random() * 2)

    def add_model(self):
        textures = [Texture() for _ in range(random.randint(1, 3))]
        for texture in textures:
            self._database_access.add_entity(texture)
        model = Model3D(textures)
        self._database_access.add_entity(model)

    def remove_model(self, model: Model3D):
        for texture in model.textures:
            self._database_access.remove_entity(texture)
        self._database_access.remove_entity(model)
