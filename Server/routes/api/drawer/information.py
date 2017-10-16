from flask_restful_swagger_2 import Resource, request, swagger

from db.models.user import UserModel
from routes.api.drawer import information_doc


class Information(Resource):
    @swagger.doc(information_doc.INFORMATION)
    def post(self):
        phone = request.form.get('phone')
        name = request.form.get('name')
        age = request.form.get('age', type=int)
        affiliation = request.form.get('affiliation')
        score = request.form.get('score', type=int)

        UserModel(phone=phone, name=name, age=age, affiliation=affiliation, score=score).save()

        image = request.files['image']
        image.save('/user_images/{0}.png'.format(phone))

        return '', 201
