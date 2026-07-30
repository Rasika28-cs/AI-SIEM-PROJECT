from django.urls import path

from . import views
from .api import login_api, logout_api, register_api

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("login/api/", login_api, name="login_api"),
    path("logout/api/", logout_api, name="logout_api"),
    path("register/api/", register_api, name="register_api"),
]