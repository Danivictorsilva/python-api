from flask_restx import Resource
from src.config.server import server
from src.services.WeatherService import WeatherService
from src.schemas.Cep import cep
api = server.api


@api.route('/api/weather')
class RegisterResource(Resource):
    @api.expect(cep.schema)
    def post(self):
        cep = api.payload['cep']


        return WeatherService.FourDaysForecast(cep)
