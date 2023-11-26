from __future__ import annotations

from homework1.in_memory_model.model_changed_observer import IModelChangedObserver
from homework1.in_memory_model.model_changer import IModelChanger
from homework1.model_elements.polygonal_model import PolygonalModel
from homework1.model_elements.scene import Scene
from homework1.model_elements.flash import Flash
from homework1.model_elements.camera import Camera


class ModelStore(IModelChanger):
    def __init__(self):
        self.__subscribers: list[IModelChangedObserver] = []
        self._models: list[PolygonalModel] = []
        self._scenes: list[Scene] = []
        self._flashes: list[Flash] = []
        self._cameras: list[Camera] = []

    def subscribe(self, subscriber: IModelChangedObserver):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: IModelChangedObserver):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)

    def _notify_change(self):
        for subscriber in self.__subscribers:
            subscriber.apply_update_model()

    def add_model(self, model: PolygonalModel):
        self._models.append(model)
        self._notify_change()

    @property
    def models(self):
        return self._models

    def add_scene(self, scene: Scene):
        self._scenes.append(scene)
        self._notify_change()

    @property
    def scenes(self):
        return self._scenes

    def add_flash(self, flash: Flash):
        self._flashes.append(flash)
        self._notify_change()

    @property
    def flashes(self):
        return self._models

    def add_camera(self, camera: Camera):
        self._cameras.append(camera)
        self._notify_change()

    @property
    def cameras(self):
        return self._cameras
