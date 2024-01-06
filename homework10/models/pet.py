from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class Pet:
    pet_id: int | None
    client_id: int
    name: str
    birthday: date

    def as_dict(self):
        return asdict(self)
