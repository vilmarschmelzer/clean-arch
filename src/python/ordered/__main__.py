from flask import Flask
from flask_restful import Api

from .http.request import RequestApi
from .httpclient import ProductClient
from .repos import RequestsRepo
from .usecases.request import RequestUseCases


def main():
    app = Flask(__name__)
    api = Api(app)

    product_client = ProductClient('http://127.0.0.1:8000/product')
    requests_repo = RequestsRepo()
    request_ucs = RequestUseCases(requests_repo, product_client)

    api.add_resource(
        RequestApi,
        '/request',
        '/request/<int:request_id>',
        resource_class_kwargs={
            'ucs': request_ucs,
        }
    )

    return app


if __name__ == '__main__':
    app = main()
    app.run(host='0.0.0.0', port=8001)
