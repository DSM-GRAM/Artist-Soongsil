from flask_restful_swagger_2 import Resource, request, swagger

from db.models.user import UserModel


class Information(Resource):
    def post(self):
        phone = request.form.get('phone')
        name = request.form.get('name')
        age = request.form.get('age', type=int)
        affiliation = request.form.get('affiliation', type=int)
        score = request.form.get('score', type=int)

        UserModel(phone=phone, name=name, age=age, affiliation=affiliation, score=score).save()

        image = request.files['image']
        image.save('/user_images/{0}.png'.format(phone))

        return '', 201
