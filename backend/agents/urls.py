from django.urls import path

from .views import agents_view, register_agent
from .api import agents_api

urlpatterns = [

    path("", agents_view, name="agents"),
    path("api/", agents_api, name="agents_api"),
    path("register/", register_agent, name="register_agent"),

]