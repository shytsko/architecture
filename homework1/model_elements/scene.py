from homework1.model_elements.flash import Flash
from homework1.model_elements.polygonal_model import PolygonalModel
from homework1.model_elements.camera import Camera
from collections.abc import Iterable


class Scene:
    __generate_id = 0

    @classmethod
    def get_next_id(cls):
        cls.__generate_id += 1
        return cls.__generate_id

    def __init__(self, name, models: Iterable[PolygonalModel], cameras: Iterable[Camera],
                 flashes: Iterable[Flash] | None = None):
        self._id = self.get_next_id()
        self._name = name
        self._models = list(models)
        if len(self._models) < 1:
            raise AttributeError('The scene must contain at least one model')
        self._cameras = list(cameras)
        if len(self._models) < 1:
            raise AttributeError('The scene must contain at least one camera')
        self._flashes = list(flashes) if flashes else []

    def add_model(self, model: PolygonalModel):
        self._models.append(model)

    def add_camera(self, camera: Camera):
        self._cameras.append(camera)

    def add_flash(self, flash: Flash):
        self._flashes.append(flash)
