from pymongo import MongoClient
from dotenv import dotenv_values
envVariables = dotenv_values(".env")
client = MongoClient(envVariables['DATABASE_CONNECTION'])

db = client[str(envVariables['DATABASE_NAME'])]
