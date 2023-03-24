from django.urls import path
from .import views
from .import office
from .import agents

urlpatterns = [
    ## test url
    ## mpesa test oauth_success
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('v1/c2b/confirmation', views.confirmation),
    path('mpesa/cipher', views.mpesa_cipher),
    # path('mpesa/token/', views.oauth_success),

    ### register urls
    path('v1/c2b/confirmation_urls', views.register_urls),

     ### MPESA - OFFICE
    path('v1/mpesa', office.mpesaList),
    path('v1/mpesa/<int:id>', office.mpesabyid),
    path('v1/mpesa/update/<int:id>', office.mpesaUpdate ),
    path('v1/mpesa/delete/<int:id>', office.mpesaDelete ),
    path('v1/mpesa/search/<str:cod>', office.mpesaSearch ),
    path('v1/mpesa/office/stat', office.mpesaOfficeStat ),
    path('v1/mpesa/office/stat/today', office.mpesaFilterToday ),
    path('v1/mpesa/office/stat/week', office.mpesaFilterWeek ),
    path('v1/mpesa/office/stat/month', office.mpesaFilterMonth ),
    path('v1/mpesa/office/stat/year', office.mpesaFilterYear ),
    path('v1/mpesa/office/stat/range', office.mpesaFilterRange ),
    ### AGENTS
    path('v1/mpesa/agents_list', office.mpesaAgentList ),
    path('v1/mpesa/agents_statistics', office.mpesaAgentStatic ),
    path('v1/mpesa/agent/search/<str:query>', office.mpesaAgentSearch ),
    path('v1/mpesa/agent/cipher', agents.agent_mpesa_cipher ),
    path('v1/mpesa/agent/pay', agents.agent_lipa_na_mpesa ),
]