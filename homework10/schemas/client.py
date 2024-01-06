from pydantic import BaseModel
from datetime import date


class ClientBase(BaseModel):
    document: str
    sur_name: str
    first_name: str
    patronymic: str
    birthday: date


class ClientIn(ClientBase):
    pass


class ClientOut(ClientBase):
    client_id: int


class ClientUpdate(BaseModel):
    client_id: int
    document: str | None = None
    sur_name: str | None = None
    first_name: str | None = None
    patronymic: str | None = None
    birthday: date | None = None
