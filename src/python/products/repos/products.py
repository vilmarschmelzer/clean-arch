from typing import List

from libs.exceptions import NotFound

from products.entities import Product as ProductEntitie
from products.entities import ProductsIfRepo

from .adapters import product_productentitie, productentitie_product
from .models import Product


class ProductsRepo(ProductsIfRepo):

    def get_all(self) -> List[ProductEntitie]:
        query = Product.select()

        data = []
        for product in list(query):
            data.append(product_productentitie(product))
        return data

    def get(self, product_id: int) -> ProductEntitie:
        try:
            return product_productentitie(
                Product.get(
                    Product.id == product_id
                )
            )
        except Product.DoesNotExist:
            raise NotFound

    def create(self, product_entitie: ProductEntitie) -> ProductEntitie:
        product = productentitie_product(product_entitie)
        product.save()
        return product_productentitie(product)

    def update(self, product_entitie: ProductEntitie) -> ProductEntitie:
        product = productentitie_product(product_entitie)
        product.save()
        return product_productentitie(product)

    def delete(self, product_id: int) -> bool:
        product = Product.get(Product.id == product_id)
        product.delete_instance()
        return product_productentitie(product)
