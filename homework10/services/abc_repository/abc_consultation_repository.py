from abc import ABC
from services.abc_repository.abc_repository import ABCRepository
from models.consultation import Consultation


class ABCConsultationRepository(ABCRepository[Consultation, int], ABC):
    pass
