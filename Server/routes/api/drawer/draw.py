import uuid

from flask_restful_swagger_2 import Resource, request, swagger

from routes.api.drawer import draw_doc
from support.fcm import fcm


class Draw(Resource):
    @swagger.doc(draw_doc.DRAW)
    def post(self):
        shower_id = request.form.get('shower_id')

        fcm.notify_single_device(registration_id=shower_id, message_title={'type': 1})

        return '', 201


class Score(Resource):
    @swagger.doc(draw_doc.SCORE)
    def post(self):
        # Need more implement
        user_image = request.files['image']
        user_image_name = '{0}.png'.format(uuid.uuid4())
        user_image.save(user_image_name)

        origin_image_name = request.form.get('origin_image_name')
