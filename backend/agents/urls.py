from django.urls import path

from .views import agents_view, register_agent
from .api import agents_api, heartbeat_api

urlpatterns = [

    path("register/", register_agent, name="register_agent"),

    path("", agents_view, name="agents"),

    path("api/", agents_api, name="agents_api"),

    path("api/heartbeat/", heartbeat_api, name="heartbeat_api"),

]