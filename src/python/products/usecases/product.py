from typing import List

from dataclasses import dataclass

from products.entities import (
    Product,
    ProductsIfRepo,
    CategoriesIfRepo
)
from libs.exceptions import NotFound, BadRequest


@dataclass
class CreateProductRequest:
    name: str
    category_id: int


@dataclass
class UpdateProductRequest:
    id: int
    name: str
    category_id: int


@dataclass
class GetProductRequest:
    id: int


@dataclass
class DeleteProductRequest:
    id: int


class ProductUseCases:
    def __init__(
            self,
            repo: ProductsIfRepo,
            repo_category: CategoriesIfRepo):

        self.repo = repo
        self.repo_category = repo_category

    def get_all(self) -> List[Product]:
        products = self.repo.get_all()

        for product in products:
            category = self.repo_category.get(product.category_id)
            product.category = category

        return products

    def get(self, req: GetProductRequest) -> Product:
        product = self.repo.get(req.id)
        category = self.repo_category.get(product.category_id)
        product.category = category
        return product

    def _exist_category(self, category_id):
        try:
            self.repo_category.get(category_id)
        except NotFound:
            raise BadRequest(
                payload={
                    'category_id': category_id,
                    'msg': 'Not found'
                }
            )

    def create(self, req: CreateProductRequest) -> Product:
        self._exist_category(req.category_id)
        return self.repo.create(
            Product(
                name=req.name,
                category_id=req.category_id,
            )
        )

    def update(self, req: UpdateProductRequest) -> Product:
        product = self.repo.get(req.id)
        self._exist_category(req.category_id)

        product.name = req.name
        product.category_id = req.category_id

        self.repo.update(product)
        category = self.repo_category.get(product.category_id)
        product.category = category
        return product

    def delete(self, req: DeleteProductRequest) -> Product:
        return self.repo.delete(req.id)
