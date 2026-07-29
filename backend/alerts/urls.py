from django.urls import path
from .detail_api import alert_detail_api, update_status_api
from .api import alerts_api
from . import views

urlpatterns = [
    path("", views.alerts_view, name="alerts"),
    path("api/", alerts_api, name="alerts_api"),
    path("<int:pk>/", views.alert_detail, name="alert_detail"),
    path("<int:pk>/status/", views.update_status, name="update_status"),
    path("api/<int:pk>/", alert_detail_api, name="alert_detail_api"),
    path("api/<int:pk>/status/", update_status_api, name="update_status_api"),
]