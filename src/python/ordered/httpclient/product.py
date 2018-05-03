from http import HTTPStatus

from libs.exceptions import NotFound
from requests import Session

from ordered.entities import Product


class ProductClient():

    def __init__(self, resource, session=None):
        self.resource = resource
        self.session = session
        if not self.session:
            self.session = Session()

    def get(self, product_id):
        response = self.session.get(self.resource + '/' + str(product_id))

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFound

        data = response.json()
        return Product(
            id=data.get('id'),
            name=data.get('name')
        )
