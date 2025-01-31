from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .social_view import facebook_oauth_redirect, google_oauth_redirect

urlpatterns = [
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "social-auth/", include("social_django.urls", namespace="social")
    ),  # api бибsqlite_sequenceлиотеки social-auth-app-django
    path(
        "v1/authentication/google/", google_oauth_redirect, name="google-login-shortcut"
    ),  # регистрация и авторизация google
    path(
        "v1/authentication/facebook/", facebook_oauth_redirect, name="facebook-login-shortcut"
    ),  # регистрация и авторизация facebook
]
