from flask import send_from_directory
from flask_restful_swagger_2 import Resource, request, swagger

from routes.api.shower import image_doc


class SampleImage(Resource):
    @swagger.doc(image_doc.SAMPLE_IMAGE)
    def get(self):
        image_name = request.args.get('image_name')

        return send_from_directory('images', image_name), 200
