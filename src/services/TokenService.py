from datetime import datetime, timedelta
from dotenv import dotenv_values
envVariables = dotenv_values(".env")
import jwt
from src.config.database import db
userCollection = db.users
from werkzeug.security import check_password_hash

class TokenService:
    @classmethod
    def generate(cls, username, password):
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
