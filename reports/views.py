from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F, Sum
from django.db.models.functions import ExtractMonth, ExtractDay

from battery.models import Battery, BatterySwap, BatteryStation
from motobikes.models import Motobikes
from battery.serializers import BatterySwapSerializer

from datetime import datetime, timedelta, time
from django.utils import timezone

#bike_no
@api_view(['GET'])
def mileage_report(request):
    data = BatterySwap.objects.annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).annotate(
          amount = Count('battery_code1') * 220
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap', 'amount').order_by('-swap')
    return Response(data)


@api_view(['GET'])
def bike_reports_totals_count(request):
    query = BatterySwap.objects.all().count()
    units = query * 3.5
    mileage = query * 95
    ghg = query * 8.64
    data = {
        'units':units,
        "swaps":query,
        'mileage': mileage,
        'ghg': ghg
    }
    return Response(data)


@api_view(['GET'])
def bike_filter_today(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    data = BatterySwap.objects.filter(createdAt__range=[today_start, today_end ]).annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap').order_by('-swap')
    return Response(data)


@api_view(['GET'])
def bike_filter_week(request):
    w_date = timezone.now()
    week_date = w_date.strftime("%V")
    data = BatterySwap.objects.filter(createdAt__week=week_date).annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap').order_by('-swap')
    return Response(data)


@api_view(['GET'])
def bike_filter_month(request):
    month_date = timezone.now().month
    data = BatterySwap.objects.filter(createdAt__month=month_date).annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap').order_by('-swap')
    return Response(data)


@api_view(['GET'])
def bike_filter_year(request):
    year_date = timezone.now().year
    data = BatterySwap.objects.filter(createdAt__year=year_date).annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).annotate(
          amount = Count('battery_code1') * 220
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap', 'amount').order_by('-swap')
    return Response(data)


@api_view(['POST'])
def bike_filter_range(request):
    data = request.data
    today_start = data['fromdate']
    today_end = data['todate']
    data = BatterySwap.objects.filter(createdAt__range=[today_start, today_end ] ).annotate(
          Count('bike_no')).values('bike_no').annotate(
          ghg=Count('battery_code1') * 8.64
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).annotate(
          mileage = Count('battery_code1') * 95
          ).annotate(
          swap = Count('battery_code1')
          ).values('bike_no', 'ghg', 'units', 'mileage', 'swap').order_by('-swap')
    return Response(data)



