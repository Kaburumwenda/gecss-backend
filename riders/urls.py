from django.urls import path

from .import views

urlpatterns = [
    path('.inc/v1/riders/mini', views.riders_min_list),
    path('.inc/v1/riders/all', views.riders_list),
    path('.inc/v1/riders/create', views.riders_create.as_view()),
]