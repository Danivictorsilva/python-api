from flask_restx import Resource
from src.services.TokenService import TokenService
from src.services.RegisterService import RegisterService
from src.schemas.User import user
from src.config.server import server
api = server.api

@api.route('/api/register')
class RegisterResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        return RegisterService.register(username, password)

@api.route('/api/token')
class TokenResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        return TokenService.generate(username, password)


