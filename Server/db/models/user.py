from db.mongo import *


class User(Document):
    phone = StringField(primary_key=True)
    name = StringField(required=True)
    age = IntField(required=True)
    score = IntField(required=True)
