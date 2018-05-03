from flask_restful import Resource, reqparse

from products.usecases.category import (
    CreateCategoryRequest,
    DeleteCategoryRequest,
    GetCategoryRequest,
    UpdateCategoryRequest
)

from .adapters import category_asdict

parser = reqparse.RequestParser()
parser.add_argument('name')


class CategoryApi(Resource):

    def __init__(self, *args, ucs=None, **kwargs):
        print(kwargs)
        self.ucs = ucs
        super().__init__(*args, **kwargs)

    def get(self, category_id=None):
        if category_id:
            request = GetCategoryRequest(id=category_id)
            return category_asdict(self.ucs.get(request))

        categories = self.ucs.get_all()

        data = []

        for category in categories:
            data.append(category_asdict(category))

        return data

    def post(self):
        category_dict = parser.parse_args()
        request = CreateCategoryRequest(name=category_dict.get('name'))

        return category_asdict(self.ucs.create(request))

    def put(self, category_id):
        category_dict = parser.parse_args()

        return category_asdict(
            self.ucs.update(
                UpdateCategoryRequest(
                    id=category_id,
                    name=category_dict.get('name')
                )
            )
        )

    def delete(self, category_id):
        return category_asdict(
            self.ucs.delete(
                DeleteCategoryRequest(
                    id=category_id,
                )
            )
        )
