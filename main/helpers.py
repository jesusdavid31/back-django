import datetime

import jwt
from django.conf import settings


class Helpers:
    def generate_jwt_token(payload):
        """
        Generate a JWT token
        """
        payload["exp"] = datetime.datetime.now() + datetime.timedelta(days=1)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
