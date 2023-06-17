from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F, Sum
from django.db.models.functions import  ExtractDay, ExtractMonth, ExtractYear
from django.db.models.functions import TruncDate

from battery.models import Battery, BatterySwap, BatteryStation
from motobikes.models import Motobikes
from battery.serializers import BatterySwapSerializer

from datetime import datetime, timedelta, time
from django.utils import timezone


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_report_counts(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    w_date = timezone.now()
    week_date = w_date.strftime("%V")
    month_date = timezone.now().month
    year_date = timezone.now().year

    today = BatterySwap.objects.filter(createdAt__range=[today_start, today_end ] ).count()
    week = BatterySwap.objects.filter(createdAt__week=week_date).count()
    month = BatterySwap.objects.filter(createdAt__month=month_date).count()
    year = BatterySwap.objects.filter(createdAt__year=year_date).count()
    total = BatterySwap.objects.all().count()
    data = {
       'today':today,
       'week':week,
       'month':month,
       'year': year,
       'total':total
    }
    return Response(data)


@api_view(['GET'])
def battery_report(request):
    data = BatterySwap.objects.annotate(
          Count('battery_code1')).values('battery_code1').annotate(
          swap=Count('battery_code1')
          ).annotate(
          amount = Count('battery_code1') * 220
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).values('battery_code1','swap', 'units', 'amount').order_by('-swap')
    return Response(data)


@api_view(['GET'])
def battery_report_min(request):
    data = BatterySwap.objects.annotate(
          Count('battery_code1')).values('battery_code1').annotate(
          swap=Count('battery_code1')
          ).annotate(
          amount = Count('battery_code1') * 220
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).values('battery_code1','swap', 'units', 'amount').order_by('-swap')[:25]
    return Response(data)


@api_view(['POST'])
def battery_report_search(request):
    data = request.data
    code = data['queary']
    data = BatterySwap.objects.filter(battery_code1=code).annotate(
          Count('battery_code1')).values('battery_code1').annotate(
          swap=Count('battery_code1')
          ).annotate(
          amount = Count('battery_code1') * 220
          ).annotate(
          units = Count('battery_code1')* 3.5
          ).values('battery_code1','swap', 'units', 'amount').order_by('-swap')
    return Response(data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_statistics_pdf_excel(request):
    post_data = request.data
    today_start = post_data['fromdate']
    today_end = post_data['todate']

    data = BatterySwap.objects.filter(createdAt__range=[today_start, today_end ]).annotate(
        date=TruncDate('createdAt')).values('date').annotate(
        day=ExtractDay('createdAt')).annotate(
        month=ExtractMonth('createdAt')).annotate(
        year=ExtractYear('createdAt')).annotate(
        total=Sum('amount')).annotate(
        swaps = Count('battery_code1')
          ).annotate(
        power_units_kw = Count('battery_code1')* 3.5
          ).annotate(
        ghg=Count('battery_code1') * 8.64
          ).values('day', 'month', 'year', 'date', 'swaps', 'total', 'power_units_kw', 'ghg').order_by('date')
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_statistics_week(request):
    w_date = timezone.now()
    this_week = w_date.strftime("%V")
    data = BatterySwap.objects.filter(
        createdAt__week=this_week).annotate(
        date=TruncDate('createdAt')).values('date').annotate(
        day=ExtractDay('createdAt')).annotate(
        month=ExtractMonth('createdAt')).annotate(
        year=ExtractYear('createdAt')).annotate(
        total=Sum('amount')).annotate(
        swaps = Count('battery_code1')
          ).annotate(
        power_units_kw = Count('battery_code1')* 3.5
          ).annotate(
        ghg=Count('battery_code1') * 8.64
          ).values('day', 'month', 'year', 'date', 'swaps', 'total', 'power_units_kw', 'ghg')
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_statistics_month(request):
    this_month = timezone.now().month
    data = BatterySwap.objects.filter(
        createdAt__month=this_month).annotate(
        date=TruncDate('createdAt')).values('date').annotate(
        day=ExtractDay('createdAt')).annotate(
        month=ExtractMonth('createdAt')).annotate(
        year=ExtractYear('createdAt')).annotate(
        total=Sum('amount')).annotate(
        swaps = Count('battery_code1')
          ).annotate(
        power_units_kw = Count('battery_code1')* 3.5
          ).annotate(
        ghg=Count('battery_code1') * 8.64
          ).values('day', 'month', 'year', 'date', 'swaps', 'total', 'power_units_kw', 'ghg')
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_statistics_year(request):
    this_year = timezone.now().year
    data = BatterySwap.objects.filter(
        createdAt__year=this_year).annotate(
        month=ExtractMonth('createdAt')).values('month').annotate(
        year=ExtractYear('createdAt')).annotate(
        total=Sum('amount')).annotate(
        swaps = Count('battery_code1')
          ).annotate(
        power_units_kw = Count('battery_code1')* 3.5
          ).annotate(
        ghg=Count('battery_code1') * 8.64
          ).values('month', 'year','swaps', 'total', 'power_units_kw', 'ghg').order_by('month')
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def battery_statistics_yearly(request):
    data = BatterySwap.objects.annotate(
        year=ExtractYear('createdAt')).values('year').annotate(
        total=Sum('amount')).annotate(
        swaps = Count('battery_code1')
          ).annotate(
        power_units_kw = Count('battery_code1')* 3.5
          ).annotate(
        ghg=Count('battery_code1') * 8.64
          ).values('year','swaps', 'total', 'power_units_kw', 'ghg')
    return Response(data)
