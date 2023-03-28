from flask_restx import Resource

from src.config.server import server


users = [
    {'id': 0, 'name': 'Daniel'}
]

api = server.api

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'users': users}


