from db.mongo import *


class DeviceModel(Document):
    registration_id = StringField(primary_key=True)
    status = IntField(required=True)
