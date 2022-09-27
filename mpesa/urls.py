from django.urls import path
from .import views
from .import office

urlpatterns = [
    ## test url
    ## mpesa test oauth_success
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('mpesa/confirmation', views.confirmation),
    path('mpesa/cipher', views.mpesa_cipher),
    # path('mpesa/token/', views.oauth_success),

     ### MPESA - OFFICE
    path('v1/mpesa', office.mpesaList),
    path('v1/mpesa/<int:id>', office.mpesabyid),
    path('v1/mpesa/update/<int:id>', office.mpesaUpdate ),
    path('v1/mpesa/delete/<int:id>', office.mpesaDelete ),
    path('v1/mpesa/search/<str:cod>', office.mpesaSearch ),
]