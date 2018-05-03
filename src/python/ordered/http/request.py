from http import HTTPStatus

from flask_restful import Resource, reqparse
from libs.exceptions import BadRequest, NotFound

from ordered.usecases.request import (
    CreateRequestRequest,
    DeleteRequestRequest,
    GetRequestRequest,
    Item,
    UpdateRequestRequest
)

from .adapters import response_request_asdict

parser = reqparse.RequestParser()
parser.add_argument('client')
parser.add_argument('items', type=dict, action='append')


class RequestApi(Resource):

    def __init__(self, *args, ucs=None, **kwargs):
        self.ucs = ucs
        super().__init__(*args, **kwargs)

    def get(self, request_id=None):
        if request_id:
            try:
                request = GetRequestRequest(id=request_id)
                return response_request_asdict(self.ucs.get(request))
            except NotFound:
                return None, HTTPStatus.NOT_FOUND

        requests = self.ucs.get_all()
        data = []

        for request in requests:
            data.append(response_request_asdict(request))

        return data

    def post(self):
        request_dict = parser.parse_args()

        items = []

        for item in request_dict.get('items', []):
            items.append(
                Item(
                    product_id=item.get('product_id'),
                    qtd=item.get('qtd'),
                )
            )

        request = CreateRequestRequest(
            client=request_dict.get('client'),
            items=items,
        )
        try:
            return response_request_asdict(self.ucs.create(request))
        except BadRequest as ex:
            return ex.payload, HTTPStatus.BAD_REQUEST

    def put(self, request_id):
        request_dict = parser.parse_args()

        return response_request_asdict(
            self.ucs.update(
                UpdateRequestRequest(
                    id=request_id,
                    client=request_dict.get('client')
                )
            )
        )

    def delete(self, request_id):
        return response_request_asdict(
            self.ucs.delete(
                DeleteRequestRequest(
                    id=request_id,
                )
            )
        )
