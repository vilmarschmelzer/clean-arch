from abc import ABC
from typing import List

from dataclasses import dataclass


@dataclass
class Category:
    name: str
    id: int = None


class CategoriesIfRepo(ABC):
    def get(self, uid: int) -> Category:
        raise NotImplementedError

    def get_all(self) -> List[Category]:
        raise NotImplementedError

    def create(self, category: Category) -> Category:
        raise NotImplementedError

    def update(self, category: Category) -> Category:
        raise NotImplementedError

    def delete(self, category: Category) -> bool:
        raise NotImplementedError
