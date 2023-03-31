from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app,
          version='1.0.0',
          title='Python API Challenge',
          description='An API developed for testing my practical skills on Python. It receives an zip code as imput and return the weather forecast of next 4 days as output.',
          doc='/docs',
          authorizations={
              'apikey': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'X-API-KEY'
              }
          })
