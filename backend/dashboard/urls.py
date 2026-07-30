from django.urls import path
from . import views
from .api import dashboard_api

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("api/", dashboard_api, name="dashboard_api"),
]