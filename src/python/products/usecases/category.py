from typing import List

from dataclasses import dataclass

from products.entities import CategoriesIfRepo, Category


@dataclass
class CreateCategoryRequest:
    name: str


@dataclass
class UpdateCategoryRequest:
    id: int
    name: str


@dataclass
class GetCategoryRequest:
    id: int


@dataclass
class DeleteCategoryRequest:
    id: int


class CategoryUseCases:
    def __init__(self, repo: CategoriesIfRepo):
        self.repo = repo

    def get_all(self) -> List[Category]:
        return self.repo.get_all()

    def get(self, req: GetCategoryRequest) -> Category:
        return self.repo.get(req.id)

    def create(self, req: CreateCategoryRequest) -> Category:
        return self.repo.create(
            Category(
                name=req.name,
            )
        )

    def update(self, req: UpdateCategoryRequest) -> Category:
        category = self.repo.get(req.id)
        category.name = req.name
        self.repo.update(category)
        return category

    def delete(self, req: DeleteCategoryRequest) -> Category:
        return self.repo.delete(req.id)
