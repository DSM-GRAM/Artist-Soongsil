import random

from flask_restful_swagger_2 import Resource, request, swagger

from db.models.category import CategoryModel
from db.models.device import DeviceModel
from routes.api.drawer import category_doc
from support.fcm import fcm


class Category(Resource):
    @swagger.doc(category_doc.CATEGORY)
    def get(self):
        return [{
            'category_code': category.category_code,
            'category_name': category.category_name,
            'chosen': category.chosen
        } for category in CategoryModel.objects], 200

    @swagger.doc(category_doc.CATEGORY_SELECT)
    def post(self):
        code = request.form.get('code', type=int)

        category = CategoryModel.objects(category_code=code).first()
        category.update(chosen=category.chosen + 1)

        image_names = category.image_names
        chosen_image_name = image_names[random.randrange(0, len(image_names))]
        # Chosen counting, collect image name

        shower = DeviceModel.objects(status=0).first()
        fcm.notify_single_device(registration_id=shower.registration_id, message_title={'type': 0, 'image_name': chosen_image_name})
        shower.update(status=1)
        # Push to waiting shower, renew status : 'Showing sample'

        return {'shower_id': shower.registration_id, 'image_name': chosen_image_name}, 201
        # Return shower id to chaining
