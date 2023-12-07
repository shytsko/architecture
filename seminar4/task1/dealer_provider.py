from factory import Factory


class DealerProvider:

    def __init__(self, factory: Factory):
        self._factory = factory

    def get_component(self, id_component: int):
        return self._factory.get_component(id_component)
