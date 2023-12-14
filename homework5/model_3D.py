from homework5.entity import Entity
from typing import Sequence, Iterable
from homework5.texture import Texture


class Model3D(Entity):
    _id_generator = iter(range(10000, 20000))

    def _next_id(self):
        return next(self._id_generator)

    def __init__(self, textures: Iterable[Texture]):
        self._id: int = self._next_id()
        self._textures = list(textures)

    @property
    def id(self) -> int:
        return self._id

    @property
    def textures(self) -> Sequence[Texture]:
        return self._textures

    def __str__(self):
        return f"Model3D <{self._id}>"
