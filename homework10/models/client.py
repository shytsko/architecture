from datetime import date
from dataclasses import dataclass, asdict


@dataclass
class Client:
    client_id: int | None
    document: str
    sur_name: str
    first_name: str
    patronymic: str
    birthday: date

    def as_dict(self):
        return asdict(self)
