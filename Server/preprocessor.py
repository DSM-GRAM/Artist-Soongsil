from flask_restful_swagger_2 import Api

from routes.api.drawer.category import Category


def process(app):
    api = Api(app, api_version=0.1)

    api.add_resource(Category, '/category')
