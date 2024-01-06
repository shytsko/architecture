from fastapi import APIRouter, HTTPException, status, Depends
from dependencies import get_pet_repository
from schemas.pet import PetIn, PetOut, PetUpdate
from services.abc_repository.abc_pet_repository import ABCPetRepository
from models.pet import Pet

pet_router = APIRouter(prefix='/pet', tags=['Pet API'])


@pet_router.get('/get-all', response_model=list[PetOut])
async def get_all(pet_repository: ABCPetRepository = Depends(get_pet_repository)):
    return [PetOut(**pet.as_dict()) for pet in pet_repository.get_all()]


@pet_router.get('/get/{pet_id}', response_model=PetOut)
async def get_by_id(pet_id: int, pet_repository: ABCPetRepository = Depends(get_pet_repository)):
    pet = pet_repository.get_by_id(pet_id)
    if pet is not None:
        return PetOut(**pet.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pet with ID {pet_id} does not exist')


@pet_router.post('/create', response_model=PetOut)
async def create(new_pet_data: PetIn, pet_repository: ABCPetRepository = Depends(get_pet_repository)):
    new_pet_id = pet_repository.create(Pet(pet_id=None, **new_pet_data.model_dump()))
    new_pet = pet_repository.get_by_id(new_pet_id)

    if new_pet is not None:
        return PetOut(**new_pet.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE, detail='Failed to create new pet')


@pet_router.delete('/delete/{pet_id}')
async def delete(pet_id: int, pet_repository: ABCPetRepository = Depends(get_pet_repository)):
    if not pet_repository.delete(pet_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Pet with ID {pet_id} does not exist')


@pet_router.put('/update', response_model=PetOut)
async def update(update_pet_data: PetUpdate, pet_repository: ABCPetRepository = Depends(get_pet_repository)):
    pet = pet_repository.get_by_id(update_pet_data.pet_id)
    if pet is not None:
        pet.client_id = update_pet_data.client_id or pet.client_id
        pet.name = update_pet_data.name or pet.name
        pet.birthday = update_pet_data.birthday or pet.birthday
        if not pet_repository.update(pet):
            raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE, detail='Failed to update pet')
        return PetOut(**pet.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Pet with ID {update_pet_data.pet_id} does not exist')
