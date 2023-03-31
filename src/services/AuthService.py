from bson import json_util
from flask import Response
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from src.config.database import db
from dotenv import dotenv_values
envVariables = dotenv_values(".env")
userCollection = db.users


class AuthService:
    @classmethod
    def verifyUser(cls, username, password):
        user = userCollection.find_one({'username': username})
        if user:
            if check_password_hash(user['password'], password):
                return True
            else:
                return False
        else:
            return False

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
