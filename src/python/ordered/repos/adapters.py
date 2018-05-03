from ordered.entities import Item as ItemEntitie
from ordered.entities import Request as RequestEntitie

from .models import Item, Request


def requestentitie_request(request_entitie: RequestEntitie) -> Request:
    request = Request()
    request.id = request_entitie.id
    request.client = request_entitie.client
    request.items = []
    for item in request_entitie.items:
        request.items.append(Item(
            product_id=item.product_id,
            qtd=item.qtd,
        ))
    return request


def request_requestentitie(request: Request) -> RequestEntitie:
    return RequestEntitie(
        id=request.id,
        client=request.client,
        items=[
            ItemEntitie(
                id=item.id,
                product_id=item.product_id,
                qtd=item.qtd,
            ) for item in request.items
        ]
    )
