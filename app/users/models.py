from flask_mongoengine import MongoEngine
from ..app import app


db = MongoEngine()
db.init_app(app)

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    name = db.StringField()
    calls = db.StringField()