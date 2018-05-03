from products.entities import Category, Product


def category_asdict(category: Category) -> Category:
    return {
        'id': category.id,
        'name': category.name
    }


def product_asdict(product: Product) -> Product:
    return {
        'id': product.id,
        'name': product.name,
        'category_id': product.category_id,
    }
