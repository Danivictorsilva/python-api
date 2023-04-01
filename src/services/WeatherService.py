import requests
from unidecode import unidecode
import xmltodict

class WeatherService:
    @classmethod
    def FourDaysForecast(cls, cep):
        fetchCepResponse = requests.get(
            'https://viacep.com.br/ws/{cep}/json/'.format(cep=cep))
        if fetchCepResponse.status_code == 200:
            fetchCepResponseJson = fetchCepResponse.json()
            city = str(fetchCepResponseJson['localidade'])
            city = unidecode(city)
            city = city.lower().replace(' ', '%20')
            fetchCityResponse = requests.get(
                'http://servicos.cptec.inpe.br/XML/listaCidades?city={city}'.format(city=city))
            dto = xmltodict.parse(fetchCityResponse.content)[
                'cidades']['cidade']
            if isinstance(dto, dict):
                city_id = dto['id']
            else:
                city_id = dto[0]['id']
            fetchForecastResponse = requests.get(
                'http://servicos.cptec.inpe.br/XML/cidade/{city_id}/previsao.xml'.format(city_id=city_id))
            fetchForecastResponseJson = xmltodict.parse(
                fetchForecastResponse.content)
            return {**fetchCepResponseJson, **fetchForecastResponseJson}
        else:
            return None
