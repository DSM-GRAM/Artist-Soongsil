from flask_restful_swagger_2 import Api

from routes.api.drawer.category import Category
from routes.api.drawer.draw import Draw, Score
from routes.api.drawer.information import Information

from routes.api.leaderboard.rank import Ranking, UserDrewImage

from routes.api.shower.device import Device
from routes.api.shower.image import SampleImage


def process(app):
    api = Api(app, api_version=0.1)

    api.add_resource(Category, '/category')
    api.add_resource(Draw, '/draw')
    api.add_resource(Score, '/score')
    api.add_resource(Information, '/information')

    api.add_resource(Ranking, '/ranking')
    api.add_resource(UserDrewImage, '/user-image')

    api.add_resource(Device, '/device')
    api.add_resource(SampleImage, '/sample-image')
