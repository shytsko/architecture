from homework1.model_elements.point_3d import Point3D
from homework1.model_elements.angle_3d import Angle3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D):
        self._location = location
        self._angle = angle

    @property
    def location(self):
        return self._location

    @property
    def angle(self):
        return self._angle

    def rotate(self, angle: Angle3D):
        self._angle = angle

    def move(self, point: Point3D):
        self._location = point
