from django.urls import path
from .import views
from .import agents

urlpatterns = [
    ### AGENT APP
    path('v1/hrms/agent_payment_list', agents.agentPaymentList),
    ### OFFICE
    path('v1/hrms/agent_payment', views.agentPayment),
    path('v1/hrms/agent_payment/<int:id>', views.agentPaymentbyid ),
    path('v1/hrms/agent_payment/create', views.AgentPaymentCreate.as_view()),
    path('v1/hrms/agent_payment/update/<int:id>', views.agentPaymentUpdate ),
    path('v1/hrms/agent_payment/search/<str:cod>', views.agentPaymentSearch  ),
    path('v1/hrms/agent_payment/delete/<int:id>', views.agentPaymentDelete ),
]