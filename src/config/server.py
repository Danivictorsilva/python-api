from flask import Flask
from flask_restx import Api


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0.0',
                       title='Python API Challenge',
                       description='An API developed for testing my practical skills on Python. It receives an zip code as imput and return the last 4 days forecast as output.',
                       doc='/docs')
        self.user_ns = self.api.namespace(name='Users', path='/')

    def run(self):
        self.app.run(debug=True, port=5000, host='0.0.0.0')


server = Server()
