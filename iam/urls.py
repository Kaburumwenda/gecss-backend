from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .import views
from .import office

urlpatterns = [
    path('v1/auth/register', views.RegisterView.as_view()),
    path('v1/auth/login', obtain_auth_token),
    path('v1/notifications', views.userNotification),

    ### MANAGEMENT
    path('v1/users', office.userList),
    path('v1/users/<int:id>', office.userData),
    path('v1/user/update/<int:id>', office.userUpdate),
    path('v1/user/delete/<int:id>', office.userDelete),
    path('v1/user/search/<str:username>', office.userSearch ),

    ## STAFF
    path('v1/staff/usernames', office.staffUsernames),
    path('v1/staff', office.staffList ),
    path('v1/staff/accounts', office.staffAccounts),
    path('v1/staff/account/create', office.StaffAccountCreate.as_view()),
    path('v1/staff/account/<int:id>', office.staffAccountbyid),
    path('v1/staff/account/update/<int:id>', office.staffUpdate ),
    path('v1/staff/account/search/<str:cod>', office.staffSearch),
    path('v1/staff/account/delete/<int:id>', office.staffAccountDelete)
]