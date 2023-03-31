from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
from flask_restx import Resource
from flask import request, jsonify
from src.services.AuthService import AuthService
from src.services.WeatherService import WeatherService
from src.services.ElasticService import ElasticService
from src.schemas.Cep import cep
from src.schemas.User import user
from src.config.app import app, api
from dotenv import dotenv_values
envVariables = dotenv_values(".env")

app.config["JWT_SECRET_KEY"] = str(envVariables['TOKEN_SECRET'])
jwt = JWTManager(app)

@api.route('/api/login')
class LoginResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        if AuthService.verifyUser(username, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            {'error': 'invalid username or password'}, 400


@api.route('/api/register')
class RegisterResource(Resource):
    @api.expect(user.schema)
    def post(self):
        username = api.payload['username']
        password = api.payload['password']

        return AuthService.register(username, password)



@api.route('/api/weather')
class WeatherResource(Resource):
    @api.expect(cep.schema)
    @jwt_required()
    @api.doc(security='apikey')
    def post(self):
        current_user = get_jwt_identity()
        print({'current_user': current_user})
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
