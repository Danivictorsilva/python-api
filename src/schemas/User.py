from src.config.server import server
from flask_restx import fields

api = server.api

class User:
  def __init__(self):
    self.schema = api.model('User', {
        'username': fields.String(required=True),
        'password': fields.String(required=True),
    })

user = User()
