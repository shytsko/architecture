from __future__ import annotations
from abc import ABC, abstractmethod
from .database import Database
from .model_configuration import ModelConfiguration


class DbContext(ABC):
    def __init__(self, database: Database):
        self._database = database

    @abstractmethod
    def _on_model_creating(self, builder: ModelBuilder):
        pass

    def save_changes(self) -> bool:
        # TODO: Сохранение изменений в базе данных
        return True


class ModelBuilder:
    def apply_configuration(self, configuration: ModelConfiguration) -> ModelBuilder:
        # TODO: добавление конфигурации маппинга объекта некоторого типа к структуре таблицы базы данных ...
        return self
