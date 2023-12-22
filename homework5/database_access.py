from abc import ABC, abstractmethod
from homework5.entity import Entity
from typing import Sequence
from homework5.model_3D import Model3D
from homework5.texture import Texture


class DatabaseAccess(ABC):
    @abstractmethod
    def add_entity(self, entity: Entity):
        pass

    @abstractmethod
    def remove_entity(self, entity: Entity):
        pass

    @abstractmethod
    def get_all_texture(self) -> Sequence[Texture]:
        pass

    @abstractmethod
    def get_all_model(self) -> Sequence[Model3D]:
        pass
