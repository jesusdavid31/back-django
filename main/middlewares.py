import jwt
from django.conf import settings
from django.http import JsonResponse


class JWTAuthenticationMiddleware:
    """
    Middleware to authenticate users based on JWT tokens.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Omitir rutas innecesarias
        exclude_paths = ["/api/user/login", "/api/user/register"]

        if request.path in exclude_paths:
            return self.get_response(request)

        # Get the JWT token from the request headers
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JsonResponse(
                {"status": "error", "message": "Authorization header missing"}
            )

        token = auth_header

        if token:
            try:
                # Decode the token using the secret key
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                request.user = payload
            except jwt.ExpiredSignatureError:
                return JsonResponse({"error": "Token has expired"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)

        response = self.get_response(request)
        return response
