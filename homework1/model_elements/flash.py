from homework1.model_elements.point_3d import Point3D
from homework1.model_elements.angle_3d import Angle3D
from homework1.model_elements.color import Color


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self._location = location
        self._angle = angle
        self._color = color
        self._power = power

    @property
    def location(self):
        return self._location

    @property
    def angle(self):
        return self._angle

    @property
    def color(self):
        return self._color

    @property
    def power(self):
        return self._power

    def rotate(self, angle: Angle3D):
        self._angle = angle

    def move(self, point: Point3D):
        self._location = point
