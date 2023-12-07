from abc import ABC, abstractmethod

from component_info import ComponentInfo


class Factory(ABC):
    @abstractmethod
    def get_component(self, id_component: int) -> ComponentInfo:
        pass
