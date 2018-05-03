from abc import ABC
from typing import List

from dataclasses import dataclass

from .item import Item


@dataclass
class Request:
    client: str
    items: List[Item]
    id: int = None

    def add(self, item):
        self.items.append(item)


class RequestsIfRepo(ABC):
    def get(self, uid: int) -> Request:
        raise NotImplementedError

    def get_all(self) -> List[Request]:
        raise NotImplementedError

    def create(self, request: Request) -> Request:
        raise NotImplementedError

    def update(self, request: Request) -> Request:
        raise NotImplementedError

    def delete(self, request: Request) -> bool:
        raise NotImplementedError
