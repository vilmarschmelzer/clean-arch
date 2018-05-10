from http import HTTPStatus

from flask_restful import Resource, reqparse
from libs.exceptions import BadRequest, NotFound

from products.usecases.product import (
    CreateProductRequest,
    DeleteProductRequest,
    GetProductRequest,
    UpdateProductRequest
)

from .adapters import product_asdict

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('category_id')


class ProductApi(Resource):

    def __init__(self, *args, ucs=None, **kwargs):
        self.ucs = ucs
        super().__init__(*args, **kwargs)

    def get(self, product_id=None):
        if product_id:
            request = GetProductRequest(id=product_id)
            try:
                return product_asdict(self.ucs.get(request))
            except NotFound:
                return None, HTTPStatus.NOT_FOUND

        products = self.ucs.get_all()

        data = []

        for product in products:
            data.append(product_asdict(product))

        return data

    def post(self):
        product_dict = parser.parse_args()
        request = CreateProductRequest(
            name=product_dict.get('name'),
            category_id=product_dict.get('category_id')
        )
        try:
            return product_asdict(self.ucs.create(request))
        except BadRequest as ex:
            return ex.payload, HTTPStatus.BAD_REQUEST

    def put(self, product_id):
        product_dict = parser.parse_args()
        request = UpdateProductRequest(
            id=product_id,
            name=product_dict.get('name'),
            category_id=product_dict.get('category_id')
        )
        try:
            return product_asdict(
                self.ucs.update(
                    request
                )
            )
        except BadRequest as ex:
            return ex.payload, HTTPStatus.BAD_REQUEST
        except NotFound as ex:
            return None, HTTPStatus.NOT_FOUND

    def delete(self, product_id):
        try:
            return product_asdict(
                self.ucs.delete(
                    DeleteProductRequest(
                        id=product_id,
                    )
                )
            )
        except NotFound:
            return None, HTTPStatus.NOT_FOUND
