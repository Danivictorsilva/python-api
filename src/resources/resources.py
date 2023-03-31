import datetime
from flask_jwt_extended import get_current_user, jwt_required, create_access_token, get_jwt_identity, JWTManager, verify_jwt_in_request
from flask_restx import Resource
from flask import Response, request, jsonify, make_response
from src.services.AuthService import AuthService
from src.services.WeatherService import WeatherService
from src.services.ElasticService import ElasticService
from src.schemas.Cep import cep
from src.schemas.User import user
from src.config.app import app, api
from functools import wraps
from dotenv import dotenv_values
envVariables = dotenv_values(".env")

app.config["JWT_SECRET_KEY"] = str(envVariables['TOKEN_SECRET'])
jwt = JWTManager(app)

def saveLog(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        current_user = get_jwt_identity()
        ElasticService.storeRequest(current_user, str(request.data), str(request.headers))
        return func(*args, **kwargs)
    return decorated

@api.route('/api/login')
class LoginResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        if AuthService.verifyUser(username, password):
            access_token = create_access_token(identity=username, expires_delta=False)
            return {'success': 'true', 'access_token': access_token}, 200
        else:
            return {'success': 'false', 'error': 'Invalid username or password'}, 400

@api.route('/api/register')
class RegisterResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']
        success = AuthService.register(username, password)
        if success:
          return {'success': 'true'}, 201
        else:
            return {'success': 'false', 'error': 'Username already exists'}, 400


@api.route('/api/weather')
class WeatherResource(Resource):
    @api.expect(cep.schema)
    @jwt_required()
    @api.doc(security='apikey')
    @saveLog
    def post(self):
        cep = api.payload['cep']
        data = WeatherService.FourDaysForecast(cep)
        if data:
          return {'success': 'true', 'data': data}, 200
        else:
            return {'success': 'false', 'error': 'Bad Request'}, 400


@api.route('/api/logs')
class LoggerResource(Resource):
    @jwt_required()
    @api.doc(security='apikey')
    def get(self):
        data = ElasticService.getUserLogs(get_jwt_identity())
        if data:
          return {'success': 'true', 'data': data}, 200
        else:
            return {'success': 'false', 'error': 'Username already exists'}, 400







