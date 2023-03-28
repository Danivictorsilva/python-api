from flask_restx import Resource
from src.config.server import server
api = server.api

from config.db import db

users = db.users

@api.route('/register')
class RegisterResource(Resource):
    def post(self):
        response = api.payload
        users.insert_one({'name': response.name})
        return response, 200

@api.route('/token')
class TokenResource(Resource):
    def post(self):
        response = api.payload
        users.insert_one({'name': response.name})
        return response, 200