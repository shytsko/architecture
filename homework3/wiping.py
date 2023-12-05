from abc import ABC, abstractmethod


class Wiping(ABC):
    @abstractmethod
    def wip_mirrors(self):
        pass

    @abstractmethod
    def wip_windshield(self):
        pass

    @abstractmethod
    def wip_head_lights(self):
        pass
