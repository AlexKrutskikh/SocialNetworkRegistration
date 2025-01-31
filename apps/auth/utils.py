from django.http import HttpResponseRedirect
from rest_framework_simplejwt.tokens import RefreshToken
from social_core.exceptions import AuthException

"""Генерирует JWT-токены, устанавливает их в cookies и перенаправляет на заданный URL"""


def generate_token_and_redirect(user, redirect_url):

    if user is None:
        raise AuthException("User does not exist or was not found.")

    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    jwt_tokens = {"access": str(access_token), "refresh": str(refresh)}

    response = HttpResponseRedirect(redirect_url)

    response.set_cookie("access_token", jwt_tokens["access"], httponly=True, secure=True, samesite=None)
    response.set_cookie("refresh_token", jwt_tokens["refresh"], httponly=True, secure=True, samesite=None)

    return response
