from django.urls import path
from . import views

urlpatterns = [
    path("", views.alerts_view, name="alerts"),
    path("<int:pk>/", views.alert_detail, name="alert_detail"),
    path("<int:pk>/status/", views.update_status, name="update_status"),
]