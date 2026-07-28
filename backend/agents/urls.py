from django.urls import path
from .views import agents_view, register_agent


urlpatterns = [

    path("register/", register_agent, name="register_agent"),
    path("", agents_view, name="agents"),

]