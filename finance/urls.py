from django.urls import path
from .import views
from .import office

urlpatterns = [
    path('v1/user/transaction', views.userTransaction),
    path('v1/user/account', views.userAccounts),

    #### OFFICE 
    path('v1/accounts', office.userAccountList),
    path('v1/account/<int:id>', office.userAccountbyid),
    path('v1/account/create', office.UserAccountCreate.as_view()),
    path('v1/account/delete/<int:id>', office.userAccountDelete),
    path('v1/account/update/<int:id>', office.userAccountUpdate ),
    path('v1/account/search/<str:username>', office.userAccountSearch ),

    ### TRANSACTIONS
    path('v1/transactions', office.transactionList),
    path('v1/transaction/<int:id>', office.transactionbyid),
    path('v1/transaction/create', office.TransactionCreate.as_view()),
    path('v1/transaction/update/<int:id>', office.transactionUpdate ),
    path('v1/transaction/delete/<int:id>', office.transactionDelete ),
    path('v1/transaction/search/<str:cod>', office.transactionSearch ),
]