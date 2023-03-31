from uuid import uuid4
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')

class ElasticService:
    @classmethod
    def storeRequest(cls, username, requestPayload, requestHeaders):
        doc = {
            'username': username,
            'req_payload': requestPayload,
            'req_headers': requestHeaders,
            'timestamp': datetime.now()
        }
        res = es.index(index='python-elasticsearch',
                       id=uuid4().hex, document=doc)

        print(res['result'])

    @classmethod
    def getUserLogs(cls, username):
        res = es.search(index='python-elasticsearch',
                        query={'match': {'username': username}})

        return list(map(lambda x: x['_source'], res['hits']['hits'])), 200
