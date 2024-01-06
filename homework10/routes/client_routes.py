from fastapi import APIRouter, HTTPException, status, Depends
from dependencies import get_client_repository
from schemas.client import ClientIn, ClientOut, ClientUpdate
from services.abc_repository.abc_client_repository import ABCClientRepository
from models.client import Client

client_router = APIRouter(prefix='/client', tags=['Client API'])


@client_router.get('/get-all', response_model=list[ClientOut])
async def get_all(client_repository: ABCClientRepository = Depends(get_client_repository)):
    return [ClientOut(**client.as_dict()) for client in client_repository.get_all()]


@client_router.get('/get/{client_id}', response_model=ClientOut)
async def get_by_id(client_id: int, client_repository: ABCClientRepository = Depends(get_client_repository)):
    client = client_repository.get_by_id(client_id)
    if client is not None:
        return ClientOut(**client.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Client with ID {client_id} does not exist')


@client_router.post('/create', response_model=ClientOut)
async def create(new_client_data: ClientIn, client_repository: ABCClientRepository = Depends(get_client_repository)):
    new_client_id = client_repository.create(Client(client_id=None, **new_client_data.model_dump()))
    new_client = client_repository.get_by_id(new_client_id)

    if new_client is not None:
        return ClientOut(**new_client.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE, detail='Failed to create new client')


@client_router.delete('/delete/{client_id}')
async def delete(client_id: int, client_repository: ABCClientRepository = Depends(get_client_repository)):
    if not client_repository.delete(client_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Client with ID {client_id} does not exist')


@client_router.put('/update', response_model=ClientOut)
async def update(update_client_data: ClientUpdate, client_repository: ABCClientRepository = Depends(get_client_repository)):
    client = client_repository.get_by_id(update_client_data.client_id)
    if client is not None:
        client.document = update_client_data.document or client.document
        client.sur_name = update_client_data.sur_name or client.sur_name
        client.first_name = update_client_data.first_name or client.first_name
        client.patronymic = update_client_data.patronymic or client.patronymic
        client.birthday = update_client_data.birthday or client.birthday
        if not client_repository.update(client):
            raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE, detail='Failed to update client')
        return ClientOut(**client.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Client with ID {update_client_data.client_id} does not exist')
