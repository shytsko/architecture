from pydantic import BaseModel
from datetime import date


class PetBase(BaseModel):
    client_id: int
    name: str
    birthday: date


class PetIn(PetBase):
    pass


class PetOut(PetBase):
    pet_id: int


class PetUpdate(BaseModel):
    pet_id: int
    client_id: int | None = None
    name: str | None = None
    birthday: date | None = None
