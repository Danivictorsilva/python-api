from uuid import uuid4
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')

class ElasticService:
    @classmethod
    def storeRequest(cls, username, endpoint, method, payload):
        doc = {
            'username': username,
            'req_url': endpoint,
            'req_method': method,
            'payload': payload,
            'timestamp': datetime.now()
        }
        res = es.index(index='python-elasticsearch',
                       id=str(uuid4()), document=doc)

        # print(res['result'])

    @classmethod
    def getUserLogs(cls, username):
        res = es.search(index='python-elasticsearch',
                        query={'match': {'username': username}})

        return list(map(lambda x: x['_source'], res['hits']['hits'])), 200
