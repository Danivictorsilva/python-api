from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')
from datetime import datetime
from uuid import uuid4


doc = {
    'username': 'daniel.silva',
    'req_url': '/api/register',
    'req_method': 'POST',
    'payload': {'key': 'value'},
    'timestamp': datetime.now()
}

# res = es.index(index='python-elasticsearch', id=str(uuid4()), document=doc)
# print(res['result'])

res = es.search(index='python-elasticsearch', query={'match': {'username': 'daniel.silva'}})


for hit in res['hits']['hits']:
    print(hit['_source'])