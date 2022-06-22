from django.urls import path
from .import views

urlpatterns = [
    path('v1/battery_stations', views.batteryStation)
]