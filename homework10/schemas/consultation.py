from pydantic import BaseModel
from datetime import datetime


class ConsultationBase(BaseModel):
    client_id: int
    pet_id: int
    date_time: datetime
    description: str


class ConsultationIn(ConsultationBase):
    pass


class ConsultationOut(ConsultationBase):
    consultation_id: int


class ConsultationUpdate(BaseModel):
    consultation_id: int
    client_id: int | None = None
    pet_id: int | None = None
    date_time: datetime | None = None
    description: str | None = None
