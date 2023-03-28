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

    def run(self):
        self.app.run(debug=True)


server = Server()
