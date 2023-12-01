from pc_components import PCComponent
from typing import Sequence


class PCServiceCard:
    def __init__(self):
        self._components: list[PCComponent] = []

    def add_component(self, component: PCComponent):
        self._components.append(component)

    def get_components(self) -> Sequence[tuple[str, int]]:
        return tuple((component.name, component.warranty) for component in self._components)
