from .point_3d import Point3D
from collections.abc import Iterable


class Polygon:
    def __init__(self, points: Iterable[Point3D]):
        self._points = set(points)
        if len(self._points) < 3:
            raise ValueError("The polygon must have at least three points")
        if len(self._points) > 3 and not self._check_plane():
            raise ValueError("All polygon points must be on the same plane")

    @property
    def points(self):
        return self.points

    def _check_plane(self):
        """
        Проверить, что все точки в self._points находятся в одной плоскости
        """
        return True
