import time
from typing import Dict
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        'access': token
    }


# Function used for signing the JWT String
def signJWT(userID: int):
    payload = {
        'user_id': userID,
        'expires_at': time.time() + 600
    }
    token = jwt.encode(payload=payload, algorithm=JWT_ALGORITHM, secrets=JWT_SECRET)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
