from abc import ABC, abstractmethod
from homework1.in_memory_model.model_changed_observer import IModelChangedObserver


class IModelChanger(ABC):

    @abstractmethod
    def subscribe(self, subscriber: IModelChangedObserver):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: IModelChangedObserver):
        pass

    @abstractmethod
    def _notify_change(self):
        pass
