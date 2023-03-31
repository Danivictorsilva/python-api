from src.config.app import api
from flask_restx import fields

class Cep:
  def __init__(self):
    self.schema = api.model('Cep', {
        'cep': fields.String(required=True),
    })

cep = Cep()
