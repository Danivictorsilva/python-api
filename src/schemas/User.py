from src.config.app import api
from flask_restx import fields

class User:
  def __init__(self):
    self.schema = api.model('User', {
        'username': fields.String(required=True, minLength=4),
        'password': fields.String(required=True, minLength=4),
    })

user = User()
