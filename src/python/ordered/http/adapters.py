from ordered.entities import Request


def request_asdict(request: Request) -> dict:
    return {
        'id': request.id,
        'client': request.client,
        'items': [
            {
                'id': item.id,
                'product_id': item.product_id,
                'qtd': item.qtd
            }
            for item in request.items
        ],
    }


def response_request_asdict(response: Request) -> dict:
    return {
        'id': response.id,
        'client': response.client,
        'items': [
            {
                'id': item.id,
                'product': {
                    'id': item.product.id,
                    'name': item.product.name
                },
                'qtd': item.qtd
            }
            for item in response.items
        ],
    }
