from src.config.database import db
userCollection = db.users
from werkzeug.security import generate_password_hash
from bson import json_util
from flask import Response

class RegisterService:
    @classmethod
    def register(cls, username, password):
        user = userCollection.find_one({'username': username})
        if user:
            return {'error': ['username already exists']}, 400
        hashed_password = generate_password_hash(password)
        userCollection.insert_one(
            {'username': username, 'password': hashed_password})
        user = userCollection.find_one({'username': username})
        response = json_util.dumps(user)
        return Response(response, mimetype="application/json", status=201)