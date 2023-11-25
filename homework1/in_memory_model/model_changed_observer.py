from abc import ABC, abstractmethod
from homework1.in_memory_model.model_changer import IModelChanger


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        """
        Получить обновление от объекта наблюдения
        """
        pass
