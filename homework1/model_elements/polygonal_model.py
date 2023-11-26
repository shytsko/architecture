from collections.abc import Iterable

from homework1.model_elements.polygon import Polygon


class PolygonalModel:
    def __init__(self, name, polygons: Iterable[Polygon], textures: Iterable[Polygon] | None = None):
        self._name = name
        self._polygons = list(polygons)
        self._textures = list(textures) if textures else []

    @property
    def polygons(self):
        return self._polygons

    @property
    def textures(self):
        return self._textures
