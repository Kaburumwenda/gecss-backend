from django.urls import path
from .import views
from .import swap_mpesa
from .import battery
from .import mpesa


urlpatterns = [
    path('v1/reports/mileage_reports', views.mileage_report),
    path('v1/reports/bike_reports', views.bike_reports_totals_count),

    ### MPESA
    path('v1/reports/mpesa_statistics/month', mpesa.mpesa_statistics_month),
    path('v1/reports/mpesa_statistics/week', mpesa.mpesa_statistics_week),
    path('v1/reports/mpesa_statistics/year', mpesa.mpesa_statistics_year),
    path('v1/reports/mpesa_statistics/yearly', mpesa.mpesa_statistics_yearly),
    path('v1/reports/mpesa_statistics/pdf_excel', mpesa.mpesa_statistics_pdf_excel),
    path('v1/reports/mpesa/list/<int:Tcounts>', mpesa.mpesa_report_List),

    #### BATTERY 
    path('v1/reports/battery_reports', battery.battery_report),
    path('v1/reports/battery_statistics/month', battery.battery_statistics_month),
    path('v1/reports/battery_statistics/week', battery.battery_statistics_week),
    path('v1/reports/battery_statistics/year', battery.battery_statistics_year),
    path('v1/reports/battery_statistics/yearly', battery.battery_statistics_yearly),
    path('v1/reports/battery_statistics/counts', battery.battery_report_counts),
    path('v1/reports/battery_statistics/min', battery.battery_report_min),
    path('v1/reports/battery_statistics/search', battery.battery_report_search),
    path('v1/reports/battery_statistics/pdf_excel', battery.battery_statistics_pdf_excel),

    ### FILTERS
    path('v1/reports/bike_reports_filter_today', views.bike_filter_today),
    path('v1/reports/bike_reports_filter_week', views.bike_filter_week),
    path('v1/reports/bike_reports_filter_month', views.bike_filter_month),
    path('v1/reports/bike_reports_filter_year', views.bike_filter_year),
    path('v1/reports/bike_reports_filter_range', views.bike_filter_range),

    ### MPESA & SWAP REPORT PIE
    path('v1/reports/swap_mpesa_pie/today', swap_mpesa.swap_mpesa_report_pie_today),
    path('v1/reports/swap_mpesa_pie/week', swap_mpesa.swap_mpesa_report_pie_week),
    path('v1/reports/swap_mpesa_pie/month', swap_mpesa.swap_mpesa_report_pie_month),
    path('v1/reports/swap_mpesa_pie/year', swap_mpesa.swap_mpesa_report_pie_year),
    path('v1/reports/swap_mpesa_pie/range', swap_mpesa.swap_mpesa_report_pie_range),
]