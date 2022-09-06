from django.urls import path
from .import views

urlpatterns = [
    ## test url
    ## mpesa test oauth_success
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('mpesa/confirmation', views.confirmation),
    # path('mpesa/token/', views.oauth_success),
]