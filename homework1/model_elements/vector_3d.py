from homework1.model_elements.point_3d import Point3D


class Vector3D:
    def __init__(self, point: Point3D):
        self._point = point

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value: Point3D):
        self._point = Point3D
