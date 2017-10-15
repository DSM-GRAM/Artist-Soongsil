from flask_restful_swagger_2 import Resource, request, swagger

from db.models.category import CategoryModel


class Category(Resource):
    def get(self):
        CategoryModel.objects.delete()

        return [{
            'category_code': category.category_code,
            'category_name': category.category_name,
            'chosen': category.chosen
        } for category in CategoryModel.objects]
