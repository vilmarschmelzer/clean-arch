from flask import Flask
from flask_restful import Api

from .http.category import CategoryApi
from .http.product import ProductApi
from .repos import CategoriesRepo, ProductsRepo
from .usecases.category import CategoryUseCases
from .usecases.product import ProductUseCases


def main():
    app = Flask(__name__)
    api = Api(app)

    categories_repo = CategoriesRepo()
    category_ucs = CategoryUseCases(categories_repo)
    products_repo = ProductsRepo()
    product_ucs = ProductUseCases(products_repo, categories_repo)

    api.add_resource(
        CategoryApi,
        '/category',
        '/category/<int:category_id>',
        resource_class_kwargs={'ucs': category_ucs}
    )

    api.add_resource(
        ProductApi,
        '/product',
        '/product/<int:product_id>',
        resource_class_kwargs={'ucs': product_ucs}
    )

    return app


if __name__ == '__main__':
    app = main()
    app.run(host='0.0.0.0', port=8000)
