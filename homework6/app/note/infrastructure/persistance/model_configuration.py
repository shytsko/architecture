from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")


class ModelConfiguration(Generic[T], ABC):
    pass
