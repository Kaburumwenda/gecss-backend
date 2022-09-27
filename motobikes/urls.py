from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('v1/motorbikes', views.motorbikeList ),
    path('v1/motorbike/<int:id>', views.motorbikebyid ),
    path('v1/motorbike/create', views.MotorbikeCreate.as_view() ),
    path('v1/motorbike/update/<int:id>', views.motorbikeUpdate ),
    path('v1/motorbike/search/<str:cod>', views.motorbikeSearch ),
    path('v1/motorbike/delete/<int:id>', views.motorbikeDelete ),
    path('v1/wandera/etr/test', views.etr_test ),
]