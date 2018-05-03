from typing import List

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str


@dataclass
class Item:
    product_id: int
    qtd: int
    id: int = None
    product: Product = None


@dataclass
class Request:
    client: str
    items: List[Item]
    id: int = None

    def add(self, item):
        self.items.append(item)


product = Product(id=1, name='product1')

item1 = Item(product_id=1, qtd=1, product=product)

caca = Item(product_id=1, qtd=1, product=item1.product)

print('caca :::: ', caca)

print(product)
print(item1)

item2 = Item(id=1, product_id=1, product=product, qtd=1)
print(item2)

request = Request(client='client1', items=[])
request.add(item1)
request.add(item2)
print(request)
