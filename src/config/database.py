from pymongo import MongoClient
import os
client = MongoClient(host='db', port=27017, connect=False)
db = client['flask_api_db']
