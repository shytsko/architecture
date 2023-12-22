import time

from homework5.business_logical_layer import BusinessLogicalLayer
from homework5.database import Database
from homework5.database_access import DatabaseAccess
from homework5.editor_business_logical_layer import EditorBusinessLogicalLayer
from homework5.editor_database import EditorDatabase
from homework5.editor_database_access import EditorDatabaseAccess
from homework5.project_file import ProjectFile
from homework5.ui_layer import UILayer


class Editor3D(UILayer):
    def __init__(self):
        self._project_file: ProjectFile | None = None
        self._business_logical_layer: BusinessLogicalLayer | None = None
        self._database_access: DatabaseAccess | None = None
        self._database: Database | None = None

    def _initialize(self):
        self._database = EditorDatabase(self._project_file)
        self._database_access = EditorDatabaseAccess(self._database)
        self._business_logical_layer = EditorBusinessLogicalLayer(self._database_access)

    def open_project(self, file_name: str):
        self._project_file = ProjectFile(file_name)
        self._initialize()
        print("Проект открыт")

    def save_project(self):
        self._database.save()
        print("Настройки сохранены")

    def show_project_settings(self):
        print("*** Настройки ***")
        print(f"file: {self._project_file.file_path}")

    def print_all_model(self):
        models = self._business_logical_layer.get_all_models()
        print("*** Модели ***")
        for model in models:
            print(model)
            for texture in model.textures:
                print(f"\t{texture}")

    def print_all_texture(self):
        textures = self._business_logical_layer.get_all_textures()
        print("*** Текстуры ***")
        for texture in textures:
            print(texture)

    def render_all(self):
        print("*** Рендеринг всех моделей ***")
        print("Рендеринг ...")
        start = time.time()
        self._business_logical_layer.render_all()
        completed_time = (time.time() - start) * 1000
        print(f"Завершено за {completed_time} ms")

    def render_model(self, model_id: int):
        print(f"*** Рендеринг модели {model_id} ***")
        models = self._business_logical_layer.get_all_models()
        for model in models:
            if model.id == model_id:
                print("Рендеринг ...")
                start = time.time()
                self._business_logical_layer.render_model(model)
                completed_time = (time.time() - start) * 1000
                print(f"Завершено за {completed_time} ms")
                break
        else:
            print("Модель не найдена")

    def add_model(self):
        print("*** Добавление модели ***")
        self._business_logical_layer.add_model()
        print("Модель добавлена")

    def remove_model(self, model_id: int):
        print("*** Удаление модели ***")
        models = self._business_logical_layer.get_all_models()
        for model in models:
            if model.id == model_id:
                self._business_logical_layer.remove_model(model)
                print(f"Модель {model_id} удалена")
                break
        else:
            print("Модель не найдена")
