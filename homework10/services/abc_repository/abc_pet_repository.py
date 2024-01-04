from abc import ABC
from services.abc_repository.abc_repository import ABCRepository
from models.pet import Pet


class ABCPetRepository(ABCRepository[Pet, int], ABC):
    pass
