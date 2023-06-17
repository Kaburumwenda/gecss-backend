from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F, Sum

from battery.models import Battery, BatterySwap
from mpesa.models import MpesaPayment


from datetime import datetime, timedelta, time
from django.utils import timezone
from home.models import GecssBranch


@api_view(['GET'])
def swap_mpesa_report_pie_today(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    swap = 0
    mpesa = 0
    swap_data = BatterySwap.objects.filter(createdAt__range=[today_start, today_end ])
    mpesa_data = MpesaPayment.objects.filter(created__range=[today_start, today_end ])

    for sd in swap_data:
        swap += sd.amount
    
    for md in mpesa_data:
        mpesa += md.transAmount

    data = {
        'swap': swap,
        'mpesa': int(mpesa),
    }

    return Response(data)


@api_view(['GET'])
def swap_mpesa_report_pie_week(request):
    w_date = timezone.now()
    week_date = w_date.strftime("%V")
    swap = 0
    mpesa = 0
    swap_data = BatterySwap.objects.filter(createdAt__week=week_date)
    mpesa_data = MpesaPayment.objects.filter(created__week=week_date)

    for sd in swap_data:
        swap += sd.amount
    
    for md in mpesa_data:
        mpesa += md.transAmount

    data = {
        'swap': swap,
        'mpesa': int(mpesa),
    }

    return Response(data)


@api_view(['GET'])
def swap_mpesa_report_pie_month(request):
    month_date = timezone.now().month
    swap = 0
    mpesa = 0
    swap_data = BatterySwap.objects.filter(createdAt__month=month_date)
    mpesa_data = MpesaPayment.objects.filter(created__month=month_date)

    for sd in swap_data:
        swap += sd.amount
    
    for md in mpesa_data:
        mpesa += md.transAmount

    data = {
        'swap': swap,
        'mpesa': int(mpesa),
    }

    return Response(data)


@api_view(['GET'])
def swap_mpesa_report_pie_year(request):
    year_date = timezone.now().year
    swap = 0
    mpesa = 0
    swap_data = BatterySwap.objects.filter(createdAt__year=year_date)
    mpesa_data = MpesaPayment.objects.filter(created__year=year_date)

    for sd in swap_data:
        swap += sd.amount
    
    for md in mpesa_data:
        mpesa += md.transAmount

    data = {
        'swap': swap,
        'mpesa': int(mpesa),
    }

    return Response(data)


@api_view(['POST'])
def swap_mpesa_report_pie_range(request):
    data = request.data
    start = data['fromdate']
    end = data['todate']
    bra_a = data['branch']
    swap = 0
    mpesa = 0
    bra_b = GecssBranch.objects.get(title=bra_a)
    branch_code = bra_b.code
    swap_data = BatterySwap.objects.filter(createdAt__range=[start, end ],  mem_no=branch_code)
    mpesa_data = MpesaPayment.objects.filter(created__range =[start, end ], billRefNumber=branch_code )

    for sd in swap_data:
        swap += sd.amount
    
    for md in mpesa_data:
        mpesa += md.transAmount

    data = {
        'swap': swap,
        'mpesa': int(mpesa),
    }

    return Response(data)