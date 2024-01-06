from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Consultation:
    consultation_id: int | None
    client_id: int
    pet_id: int
    date_time: datetime
    description: str

    def as_dict(self):
        return asdict(self)
