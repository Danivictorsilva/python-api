from datetime import datetime, timedelta
from dotenv import dotenv_values
envVariables = dotenv_values(".env")
import jwt
from src.config.database import db
userCollection = db.users
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import Response
from bson import json_util

class AuthService:
    @classmethod
    def generateToken(cls, username, password):
        user = userCollection.find_one({'username': username})
        if user:
            if check_password_hash(user['password'], password):
                return {'access_token': jwt.encode({
                    'user_id': str(user['_id']),
                    'exp': datetime.utcnow() + timedelta(minutes=30)
                }, str(envVariables['TOKEN_SECRET']))}, 200
            else:
                return {'error': ['invalid username or password']}, 400
        else:
            return {'error': ['invalid username or password']}, 400

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
