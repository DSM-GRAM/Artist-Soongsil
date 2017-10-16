from flask_restful_swagger_2 import Resource, request, swagger

from db.models.device import DeviceModel
from routes.api.shower import device_doc


class Device(Resource):
    @swagger.doc(device_doc.DEVICE)
    def post(self):
        registration_id = request.form.get('registration_id')

        DeviceModel(registration_id=registration_id, status=0).save()

        return '', 201
