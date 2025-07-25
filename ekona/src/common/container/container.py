from abc import ABC
from typing import TypeVar, Type, cast
import punq


T = TypeVar("T")


class IContainer(ABC):
    def get(self, key: Type[T]) -> T:
        raise NotImplementedError


class PunqContainer(IContainer):
    def __init__(self):
        self.container = punq.Container()

    def get(self, key: Type[T]) -> T:
        return cast(T, self.container.resolve(key))

    def register(self, *args, **kwargs):
        self.container.register(*args, **kwargs)
