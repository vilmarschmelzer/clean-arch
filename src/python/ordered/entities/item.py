from dataclasses import dataclass

from .product import Product


@dataclass
class Item:
    product_id: int
    qtd: int
    id: int = None
    product: Product = None
