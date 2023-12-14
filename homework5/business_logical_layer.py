from abc import ABC, abstractmethod
from typing import Sequence
from homework5.model_3D import Model3D
from homework5.texture import Texture


class BusinessLogicalLayer(ABC):
    @abstractmethod
    def get_all_models(self) -> Sequence[Model3D]:
        pass

    @abstractmethod
    def get_all_textures(self) -> Sequence[Texture]:
        pass

    @abstractmethod
    def render_model(self, model: Model3D):
        pass

    @abstractmethod
    def render_all(self):
        pass

    @abstractmethod
    def add_model(self):
        pass

    @abstractmethod
    def remove_model(self, model: Model3D):
        pass
