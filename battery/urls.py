from django import views
from django.urls import path

from . import agents
from .import views
from .import operations

urlpatterns =[
    path('v1/batteries', views.batteries),
    path('v1/battery/create', views.BatteryCreate.as_view() ),
    path('v1/battery/<int:id>', views.batterybyid),
    path('v1/battery/update/<int:id>', views.batteryUpdate ),
    path('v1/battery/search/<str:cod>', views.batterySearch  ),
    path('v1/battery/delete/<int:id>', views.batteryDelete),
    path('v1/battery/statistics', views.batteryStatistics),
    path('v1/battery/filters', views.batteriesFilter),

    #### BATTERY STATIONS
    path('v1/battery/stations', views.batteryStations),
    path('v1/battery/station/<int:id>', views.batteryStationbyid ),
    path('v1/battery/station/create', views.BatteryStationCreate.as_view()),
    path('v1/battery/station/update/<int:id>', views.batteryStationUpdate ),
    path('v1/battery/statiton/search/<str:cod>', views.batteryStationSearch  ),
    path('v1/battery/station/delete/<int:id>', views.batterystationDelete ),

    ### BATTERY SWAP
    path('v1/battery/swap', views.batterySwap),
    path('v1/battery/swap/create', views.BatterySwapCreate.as_view() ),
    path('v1/battery/swap/<int:id>', views.batterySwapbyid ),
    path('v1/battery/swap/update/<int:id>', views.batterySwapUpdate ),
    path('v1/battery/swap/search/<str:cod>', views.batterySwapSearch  ),
    path('v1/battery/swap/delete/<int:id>', views.batterySwapDelete ),

    #### PDF
    path('v1/battery/pdf', views.batterySwappdf ),
    path('v1/battery/pdf/today', views.batterySwappdftoday ),
    path('v1/battery/pdf/month', views.batterySwappdfmonth ),
    path('v1/battery/pdf/year', views.batterySwappdfyear ),

    #### AGENTS SWAP BATTERY
    path('v1/battery/agent/swap/statistics', agents.agent_battery_swap ),
    path('v1/battery/agent/charged', agents.agent_battery_charged ),
    path('v1/battery/agent/depleted', agents.agent_battery_depleted ),
    path('v1/battery/agent/issued', agents.agent_battery_issued ),
    path('v1/battery/agents/count', agents.agents_batteries),
    path('v1/battery/agents/swap/create', agents.BatteryAgentsSwapCreate.as_view() ),
    path('v1/battery/agents/checkbike', agents.checkbike),
    path('v1/battery/agents/retake_battery', agents.BatteryAgentsRetake.as_view() ),

    #### OPERATIONS
    path('v1/battery/operations/assign', operations.BatteryAssign.as_view() ),
    path('v1/battery/operations/charging', operations.BatteryCharging.as_view() ),
    path('v1/battery/operations/charged', operations.BatteryCharged.as_view() ), 
    path('v1/battery/operations/statistics', operations.batteryBranchStatistics ),
]