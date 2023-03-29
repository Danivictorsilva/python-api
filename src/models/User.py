from src.config.server import server
from flask_restx import fields

api = server.api

class User:
  def __init__(self):
    self.schema = api.model('User', {
        'username': fields.String(),
        'password': fields.String(),
    })

user = User()
