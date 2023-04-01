from uuid import uuid4
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'elastic', 'port': 9200}])

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

    @classmethod
    def getUserLogs(cls, username):
        res = es.search(index='python-elasticsearch',
                        query={'match': {'username': username}})

        return list(map(lambda x: x['_source'], res['hits']['hits']))
