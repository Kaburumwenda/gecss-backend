from django.urls import path
from .import views
from .import branch
from .import trends

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

    ### TOTALS
    path('v1/statistics/totals', views.totalsCount ),
    path('v1/statistics/graph', views.statisticsGraphs),

    ### AGENT NOTIFICATIONS
    path('v1/home/agent_notifications', views.agentNotificationList),
    path('v1/home/agent_notifications/<int:id>', views.agentNotificationbyid),
    path('v1/home/agent_notifications/create', views.AgentNotificationCreate.as_view()),
    path('v1/home/agent_notifications/update/<int:id>', views.agentNotificationUpdate ),
    path('v1/home/agent_notifications/delete/<int:id>', views.agentNotificationDelete ),
    path('v1/home/agent_notifications/search/<str:cod>', views.agentNotificationSearch ),

    ### COMPANY TRENDS
    path('v1/home/trends/list', trends.trendslist ),
    path('v1/home/trends/create', trends.TrendsCreate.as_view()),
    path('v1/home/trends/update/<int:id>', trends.trendsUpdate ),
    path('v1/home/trends/<int:id>', trends.trendsbyid ),
    path('v1/home/trends/search/<str:cod>', trends.trendsSearch ),
    path('v1/home/trends/delete/<int:id>', trends.trendsDelete ),

]