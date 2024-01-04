from fastapi import APIRouter, HTTPException, status, Depends
from dependencies import get_consultation_repository
from schemas.consultation import ConsultationIn, ConsultationOut, ConsultationUpdate
from services.abc_repository.abc_consultation_repository import ABCConsultationRepository
from models.consultation import Consultation

consultation_router = APIRouter(prefix='/consultation', tags=['Consultation API'])


@consultation_router.get('/get-all', response_model=list[ConsultationOut])
async def get_all(consultation_repository: ABCConsultationRepository = Depends(get_consultation_repository)):
    return [ConsultationOut(**consultation.as_dict()) for consultation in consultation_repository.get_all()]


@consultation_router.get('/get/{consultation_id}', response_model=ConsultationOut)
async def get_by_id(consultation_id: int,
                    consultation_repository: ABCConsultationRepository = Depends(get_consultation_repository)):
    consultation = consultation_repository.get_by_id(consultation_id)
    if consultation is not None:
        return ConsultationOut(**consultation.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Consultation with ID {consultation_id} does not exist')


@consultation_router.post('/create', response_model=ConsultationOut)
async def create(new_consultation_data: ConsultationIn,
                 consultation_repository: ABCConsultationRepository = Depends(get_consultation_repository)):
    new_consultation_id = consultation_repository.create(
        Consultation(consultation_id=None, **new_consultation_data.model_dump()))
    new_consultation = consultation_repository.get_by_id(new_consultation_id)

    if new_consultation is not None:
        return ConsultationOut(**new_consultation.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE,
                            detail='Failed to create new consultation')


@consultation_router.delete('/delete/{consultation_id}')
async def delete(consultation_id: int,
                 consultation_repository: ABCConsultationRepository = Depends(get_consultation_repository)):
    if not consultation_repository.delete(consultation_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Consultation with ID {consultation_id} does not exist')


@consultation_router.put('/update', response_model=ConsultationOut)
async def update(update_consultation_data: ConsultationUpdate,
                 consultation_repository: ABCConsultationRepository = Depends(get_consultation_repository)):
    consultation = consultation_repository.get_by_id(update_consultation_data.consultation_id)
    if consultation is not None:
        consultation.client_id = update_consultation_data.client_id or consultation.client_id
        consultation.pet_id = update_consultation_data.pet_id or consultation.pet_id
        consultation.date_time = update_consultation_data.date_time or consultation.date_time
        consultation.description = update_consultation_data.description or consultation.description
        if not consultation_repository.update(consultation):
            raise HTTPException(status_code=status.HTTP_507_INSUFFICIENT_STORAGE,
                                detail='Failed to update consultation')
        return ConsultationOut(**consultation.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Consultation with ID {update_consultation_data.consultation_id} does not exist')
