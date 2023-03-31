from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app,
          version='1.0.0',
          title='Python API Challenge',
          description='An API developed for testing my practical skills on Python. It receives an zip code as input and return the city weather forecast of next 4 days as output. Before requesting, log in, get the retrieved "access_token" and insert "Bearer <your_access_token>" in "Authorize" button',
          doc='/docs',
          authorizations={
              'apikey': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              }
          })
