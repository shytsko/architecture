from homework1.model_elements.vector_3d import Vector3D


class Angle3D:
    def __init__(self, vector1: Vector3D, vector2: Vector3D):
        self._vector1 = vector1
        self._vector2 = vector2

    @property
    def vector1(self):
        return self._vector1

    @property
    def vector2(self):
        return self._vector2
