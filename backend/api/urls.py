from django.urls import path
from . import views

urlpatterns = [
    path("logs/upload/", views.upload_log, name="upload_log"),
]