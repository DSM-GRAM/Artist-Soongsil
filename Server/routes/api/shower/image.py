from flask import send_from_directory
from flask_restful_swagger_2 import Resource, request, swagger


class Image(Resource):
    def get(self):
        image = request.args.get('image')

        return send_from_directory('images', image), 200
