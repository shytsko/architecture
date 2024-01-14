from clinic_api import Configuration, ApiClient, ClientApi, PetApi, ConsultationApi, ClientIn, ClientOut, ClientUpdate
from clinic_api.rest import ApiException
from datetime import date

if __name__ == '__main__':
    config = Configuration()
    config.host = 'http://127.0.0.1:8000'
    client_api = ClientApi(ApiClient(config))
    pet_api = PetApi(ApiClient(config))
    consultation_api = ConsultationApi(ApiClient(config))

    try:
        api_response = client_api.client_get_all()
        print(api_response)
    except ApiException as e:
        print("Не удалось получить информацию о всех клиентах")

    try:
        api_response = pet_api.pet_get_all()
        print(api_response)
    except ApiException as e:
        print("Не удалось получить информацию о всех животных")

    try:
        api_response = consultation_api.consultation_get_all()
        print(api_response)
    except ApiException as e:
        print("Не удалось получить информацию о всех консультациях")

    client_id = 1
    try:
        api_response = client_api.client_get_by_id(client_id)
        print(api_response)
    except ApiException as e:
        print(f"Не удалось получить информацию о клиенте c id {client_id}")

    client_id = 8
    try:
        api_response = client_api.client_get_by_id(client_id)
        print(api_response)
    except ApiException as e:
        print(f"Не удалось получить информацию о клиенте c id {client_id}")

    body = ClientIn(document='new_document', sur_name='new_client_surname', first_name='new_client_name',
                    patronymic='chgnhgng', birthday=date(2000, 1, 1))

    new_client_id = None
    try:
        api_response: ClientOut = client_api.client_create(body)
        print(api_response)
        new_client_id = api_response.client_id
    except ApiException as e:
        print("Не удалось создать клиента")

    if new_client_id is not None:
        body = ClientUpdate(client_id=new_client_id, document='11111111')
        try:
            api_response: ClientOut = client_api.client_update(body)
            print(api_response)
        except ApiException as e:
            print("Не удалось изменить данные клиента")

        try:
            api_response = client_api.client_get_by_id(new_client_id)
            print(api_response)
        except ApiException as e:
            print(f"Не удалось получить информацию о клиенте c id {client_id}")

        try:
            client_api.client_delete(new_client_id)
            print(f"Клиент с id {new_client_id} удален")
        except ApiException as e:
            print("Не удалось удалить клиента")

        try:
            api_response = client_api.client_get_by_id(new_client_id)
            print(api_response)
        except ApiException as e:
            print(f"Не удалось получить информацию о клиенте c id {client_id}")
