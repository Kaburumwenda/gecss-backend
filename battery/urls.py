from django import views
from django.urls import path
from .import views

urlpatterns =[
    path('v1/batteries', views.batteries),
    path('v1/battery/create', views.BatteryCreate.as_view() ),
    path('v1/battery/<int:id>', views.batterybyid),
    path('v1/battery/update/<int:id>', views.batteryUpdate ),
    path('v1/battery/search/<str:cod>', views.batterySearch  ),
    path('v1/battery/delete/<int:id>', views.batteryDelete),

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
]