from src.config.server import server
from flask_restx import fields

api = server.api

class Cep:
  def __init__(self):
    self.schema = api.model('Cep', {
        'cep': fields.String(required=True),
    })

cep = Cep()
