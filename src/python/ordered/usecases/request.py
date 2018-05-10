from typing import List

from dataclasses import dataclass
from libs.exceptions import BadRequest, NotFound

from ordered.entities import Item, Request, RequestsIfRepo


@dataclass
class CreateRequestRequest:
    client: str
    items: List[Item]


@dataclass
class UpdateRequestRequest:
    id: int
    client: str
    items: List[Item]


@dataclass
class GetRequestRequest:
    id: int


@dataclass
class DeleteRequestRequest:
    id: int


class RequestUseCases:
    def __init__(self, repo: RequestsIfRepo, product_client):
        self.repo = repo
        self.product_client = product_client

    def get_all(self) -> List[Request]:
        requests = self.repo.get_all()
        for request in requests:
            for item in request.items:
                try:
                    product = self.product_client.get(item.product_id)
                except NotFound:
                    continue

                item.product = product

        return requests

    def get(self, req: GetRequestRequest) -> Request:
        request = self.repo.get(req.id)
        for item in request.items:
            try:
                product = self.product_client.get(item.product_id)
            except NotFound:
                continue

            item.product = product
        return request

    def create(self, req: CreateRequestRequest) -> Request:
        self._exist_products([item.product_id for item in req.items])

        request = self.repo.create(
            Request(
                client=req.client,
                items=req.items,
            )
        )

        for item in request.items:
            try:
                product = self.product_client.get(item.product_id)
            except NotFound:
                continue

            item.product = product

        return request

    def update(self, req: UpdateRequestRequest) -> Request:
        request = self.repo.get(req.id)
        request.client = req.client
        self.repo.update(request)
        return request

    def delete(self, req: DeleteRequestRequest) -> Request:
        return self.repo.delete(req.id)

    def _exist_products(self, product_ids):
        not_found_products = []
        for product_id in product_ids:
            try:
                self.product_client.get(product_id)
            except NotFound:
                not_found_products.append(product_id)

        if not_found_products:

            errors = []
            for product_id in not_found_products:
                errors.append(
                    {
                        'items.product_id': product_id,
                        'msg': 'Not found'
                    }
                )

            raise BadRequest(payload=errors)
