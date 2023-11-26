class Texture:
    __generate_id = 0

    def __init__(self, name):
        self._name = name
        self._id = self.get_next_id()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @classmethod
    def get_next_id(cls):
        cls.__generate_id += 1
        return cls.__generate_id
