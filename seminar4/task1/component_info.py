class ComponentInfo:
    def __init__(self, component_id: int, description: str):
        self._id: int = component_id
        self._description: str = description
        self._price: float = 0

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f"{self._id} - {self._description}"
