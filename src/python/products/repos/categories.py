from typing import List

from libs.exceptions import NotFound

from products.entities import Category as CategoryEntitie
from products.entities import CategoriesIfRepo

from .adapters import category_categoryentitie, categoryentitie_category
from .models import Category


class CategoriesRepo(CategoriesIfRepo):

    def get_all(self) -> List[CategoryEntitie]:
        query = Category.select()

        data = []
        for category in list(query):
            data.append(category_categoryentitie(category))
        return data

    def get(self, category_id: int) -> CategoryEntitie:
        try:
            return category_categoryentitie(
                Category.get(
                    Category.id == category_id
                )
            )
        except Category.DoesNotExist:
            raise NotFound

    def create(self, category_entitie: CategoryEntitie) -> CategoryEntitie:
        category = categoryentitie_category(category_entitie)
        category.save()
        return category_categoryentitie(category)

    def update(self, category_entitie: CategoryEntitie) -> CategoryEntitie:
        category = categoryentitie_category(category_entitie)
        category.save()
        return category_categoryentitie(category)

    def delete(self, category_id: int) -> bool:
        category = Category.get(Category.id == category_id)
        category.delete_instance()
        return category_categoryentitie(category)
