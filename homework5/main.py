from homework5.editor_3D import Editor3D

if __name__ == '__main__':
    editor = Editor3D()
    exit_flag = False
    while not exit_flag:
        print("*** МЕНЮ ***")
        print("=======================")
        print("1. Открыть проект")
        print("2. Сохранить проект")
        print("3. Отобразить параметры проекта")
        print("4. Отобразить все модели проекта")
        print("5. Отобразить все текстуры проекта")
        print("6. Выполнить рендер всех моделей")
        print("7. Выполнить рендер модели")
        print("8. Добавить модель")
        print("9. Удалить модель")
        print("0. ЗАВЕРШЕНИЕ РАБОТЫ ПРИЛОЖЕНИЯ")
        command = input("> ")
        match command:
            case '0':
                exit_flag = True
            case '1':
                editor.open_project("file")
            case '2':
                editor.save_project()
            case '3':
                editor.show_project_settings()
            case '4':
                editor.print_all_model()
            case '5':
                editor.print_all_texture()
            case '6':
                editor.render_all()
            case '7':
                model_id = int(input("Введите id модели: "))
                editor.render_model(model_id)
            case '8':
                editor.add_model()
            case '9':
                model_id = int(input("Введите id модели: "))
                editor.remove_model(model_id)
            case _:
                print("Команда не распознана")
