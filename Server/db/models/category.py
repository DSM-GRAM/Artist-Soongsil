from db.mongo import *


class Category(Document):
    category_code = IntField(primary_key=True)
    category_name = StringField(required=True, default='이름 없는 카테고리')
    chosen = IntField(required=True, default=0)
    image_paths = ListField(StringField())
