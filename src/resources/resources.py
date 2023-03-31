from flask_jwt_extended import jwt_required
from flask_restx import Resource
from flask import request
from src.services.TokenService import TokenService
from src.services.RegisterService import RegisterService
from src.services.WeatherService import WeatherService
from src.schemas.Cep import cep
from src.schemas.User import user
from src.config.app import app, api

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



@api.route('/api/weather')
class WeatherResource(Resource):
    @api.expect(cep.schema)
    # @api.doc(security='apiKey')
    @jwt_required()
    def post(self):
        cep = api.payload['cep']
        return WeatherService.FourDaysForecast(cep)

@app.before_request
def saveOnElastic():
    if request.path.__contains__('api'):
        print({'endpoint': request.path,
               'method': request.method})