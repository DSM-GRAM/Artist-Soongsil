from flask import send_from_directory
from flask_restful_swagger_2 import Resource, request, swagger

from db.models.user import UserModel


class Ranking(Resource):
    def get(self):
        rank = [{
            'name': user.name,
            'phone': user.phone,
            'affiliation': user.affiliation,
            'score': user.score
        } for user in UserModel.objects]

        rank = sorted(rank, key=lambda k: k['score'], reverse=True)

        return rank, 200


class UserDrewImage(Resource):
    def get(self):
        phone = request.args.get('phone')

        return send_from_directory('user_images', '{0}.png'.format(phone))
