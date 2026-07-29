from django.urls import path

from .api import logs_api
from .views import logs_view

urlpatterns = [
    path("", logs_view, name="logs"),
    path("api/", logs_api, name="logs_api")
]