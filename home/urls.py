from django.urls import path
from .import views
from .import branch

urlpatterns = [
    path('v1/battery_stations', views.batteryStation),

    ### BRANCHES
    path('v1/branches', branch.CompanyBranch.as_view()),
    path('v1/branch/list', branch.branchList ),
    path('v1/branch/create', branch.BranchCreate.as_view()),
    path('v1/branch/update/<int:id>', branch.branchUpdate ),
    path('v1/branch/<int:id>', branch.companyBranchbyid ),
    path('v1/branch/search/<str:cod>', branch.branchSearch ),
    path('v1/branch/delete/<int:id>', branch.branchDelete ),
]