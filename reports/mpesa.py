from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F, Sum
from django.db.models.functions import  ExtractDay, ExtractMonth, ExtractYear
from django.db.models.functions import TruncDate

from mpesa.models import MpesaPayment
from mpesa.serializers import *

from datetime import datetime, timedelta, time
from django.utils import timezone


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_report_List(request, Tcounts):
    data = MpesaPayment.objects.all().order_by('-id')[:Tcounts]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_statistics_pdf_excel(request):
    post_data = request.data
    today_start = post_data['fromdate']
    today_end = post_data['todate']

    data = MpesaPayment.objects.filter(created__range=[today_start, today_end ]).annotate(
        Date=TruncDate('created')).values('Date').annotate(
        Day=ExtractDay('created')).annotate(
        Month=ExtractMonth('created')).annotate(
        Year=ExtractYear('created')).annotate(
        Revenue=Sum('transAmount')).values('Date','Month', 'Day', 'Year', 'Revenue').order_by('Date')
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_statistics_week(request):
    w_date = timezone.now()
    this_week = w_date.strftime("%V")
    data = MpesaPayment.objects.filter(
        created__week=this_week).annotate(
        date=TruncDate('created')).values('date').annotate(
        day=ExtractDay('created')).annotate(
        month=ExtractMonth('created')).annotate(
        year=ExtractYear('created')).annotate(
        total=Sum('transAmount')).values('day', 'month', 'year', 'date', 'total')
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_statistics_month(request):
    this_month = timezone.now().month
    data = MpesaPayment.objects.filter(
        created__month=this_month).annotate(
        date=TruncDate('created')).values('date').annotate(
        day=ExtractDay('created')).annotate(
        month=ExtractMonth('created')).annotate(
        year=ExtractYear('created')).annotate(
        total=Sum('transAmount')).values('day', 'month', 'year', 'date', 'total')
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_statistics_year(request):
    this_year = timezone.now().year
    data = MpesaPayment.objects.filter(
        created__year=this_year).annotate(
        month=ExtractMonth('created')).values('month').annotate(
        year=ExtractYear('created')).annotate(
        total=Sum('transAmount')).values('month', 'year', 'total').order_by('month')
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_statistics_yearly(request):
    data = MpesaPayment.objects.annotate(
        year=ExtractYear('created')).values('year').annotate(
        total=Sum('transAmount')).values('year', 'total')
    return Response(data)
