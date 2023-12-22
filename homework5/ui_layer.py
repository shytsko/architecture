from abc import ABC, abstractmethod


class UILayer(ABC):
    @abstractmethod
    def open_project(self, file_name: str):
        pass

    @abstractmethod
    def save_project(self):
        pass

    @abstractmethod
    def show_project_settings(self):
        pass

    @abstractmethod
    def print_all_model(self):
        pass

    @abstractmethod
    def print_all_texture(self):
        pass

    @abstractmethod
    def render_all(self):
        pass

    @abstractmethod
    def render_model(self, i: int):
        pass

    @abstractmethod
    def add_model(self):
        pass

    @abstractmethod
    def remove_model(self, model_id: int):
        pass
