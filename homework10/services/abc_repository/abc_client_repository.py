from abc import ABC
from services.abc_repository.abc_repository import ABCRepository
from models.client import Client


class ABCClientRepository(ABCRepository[Client, int], ABC):
    pass
