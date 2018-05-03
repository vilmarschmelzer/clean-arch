from typing import List

from libs.exceptions import NotFound

from ordered.entities import Request as RequestEntitie
from ordered.entities import RequestsIfRepo

from .adapters import request_requestentitie, requestentitie_request
from .models import Item, Request


class RequestsRepo(RequestsIfRepo):

    def get_all(self) -> List[RequestEntitie]:
        query = Request.select()

        data = []
        for request in list(query):
            items = Item.select().where(Item.request_id == request.id)
            request.items = list(items)
            data.append(request_requestentitie(request))
        return data

    def get(self, request_id: int) -> RequestEntitie:
        try:
            request = Request.get(
                Request.id == request_id
            )
        except Request.DoesNotExist:
            raise NotFound

        items = Item.select().where(Item.request_id == request.id)
        request.items = list(items)
        return request_requestentitie(request)

    def create(self, request_entitie: RequestEntitie) -> RequestEntitie:
        request = requestentitie_request(request_entitie)
        request.save()

        for item in request.items:
            item.request_id = request.id
            item.save()
        return request_requestentitie(request)

    def update(self, request_entitie: RequestEntitie) -> RequestEntitie:
        request = requestentitie_request(request_entitie)
        request.save()
        return request_requestentitie(request)

    def delete(self, request_id: int) -> bool:
        request = Request.get(Request.id == request_id)
        request.delete_instance()
        return request_requestentitie(request)
