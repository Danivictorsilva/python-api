from flask_jwt_extended import jwt_required
from flask_restx import Resource
from flask import request
from src.services.AuthService import AuthService
from src.services.WeatherService import WeatherService
from src.services.ElasticService import ElasticService
from src.schemas.Cep import cep
from src.schemas.User import user
from src.config.app import app, api


@api.route('/api/register')
class RegisterResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        return AuthService.register(username, password)


@api.route('/api/token')
class TokenResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        return AuthService.generateToken(username, password)


@api.route('/api/weather')
class WeatherResource(Resource):
    @api.expect(cep.schema)
    def post(self):
        cep = api.payload['cep']
        return WeatherService.FourDaysForecast(cep)


@api.route('/api/logs')
class LoggerResource(Resource):
    def get(self):
        return ElasticService.getUserLogs('daniel.silva')


@app.before_request
def saveOnElastic():
    if request.path.__contains__('api'):
        # ElasticService.storeRequest()
        print({'endpoint': request.path,
               'method': request.method})
