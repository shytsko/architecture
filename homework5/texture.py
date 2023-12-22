from homework5.entity import Entity


class Texture(Entity):
    _id_generator = iter(range(50000, 60000))

    def _next_id(self):
        return next(self._id_generator)

    def __init__(self):
        self._id: int = self._next_id()

    @property
    def id(self) -> int:
        return self._id

    def __str__(self):
        return f"Texture <{self._id}>"
