from products.entities import Category as CategoryEntitie
from products.entities import Product as ProductEntitie

from .models import Category, Product


def categoryentitie_category(category_entitie: CategoryEntitie) -> Category:
    category = Category()
    category.id = category_entitie.id
    category.name = category_entitie.name
    return category


def category_categoryentitie(category: Category) -> CategoryEntitie:
    return CategoryEntitie(
        id=category.id,
        name=category.name
    )


def productentitie_product(product_entitie: ProductEntitie) -> Product:
    product = Product()
    product.id = product_entitie.id
    product.name = product_entitie.name
    product.category = product_entitie.category_id
    return product


def product_productentitie(product: Product) -> ProductEntitie:
    return ProductEntitie(
        id=product.id,
        name=product.name,
        category_id=product.category_id,
    )
