from abc import ABC
from typing import List

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    category_id: str
    id: int = None


class ProductsIfRepo(ABC):
    def get(self, uid: int) -> Product:
        raise NotImplementedError

    def get_all(self) -> List[Product]:
        raise NotImplementedError

    def create(self, product: Product) -> Product:
        raise NotImplementedError

    def update(self, product: Product) -> Product:
        raise NotImplementedError

    def delete(self, product: Product) -> bool:
        raise NotImplementedError
