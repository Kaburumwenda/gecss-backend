from django.shortcuts import render
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F
from datetime import datetime, timedelta, time
from django.utils import timezone
# Create your views here.

##### AGENTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaAgentList(request):
    user = request.user
    data = MpesaPayment.objects.filter(billRefNumber=user).order_by('-id')[:25]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaAgentSearch(request, query):
    user = request.user
    data = MpesaPayment.objects.filter(billRefNumber=user).filter(Q(transID=query) | Q(firstName=query) )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)

### TOTALS COUNTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaAgentStatic(request):
    agent = request.user
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    w_date = timezone.now()
    week = w_date.strftime("%V")
    month_date = timezone.now().month
    year_date = timezone.now().year
    today = 0
    month = 0
    year = 0
    total = 0
    today_sum = 0
    month_sum = 0
    year_sum = 0
    total_sum = 0
    today_query = MpesaPayment.objects.filter(billRefNumber=agent, created__range=[today_start, today_end ] )
    month_query = MpesaPayment.objects.filter(created__month=month_date, billRefNumber=agent)
    year_query = MpesaPayment.objects.filter(created__year=year_date, billRefNumber=agent)
    total_query = MpesaPayment.objects.filter(billRefNumber=agent)

    for ms in today_query:
        today += ms.transAmount
        today_sum = (int(today) * 9.09091) /100
   
    for ms in month_query:
        month += ms.transAmount
        month_sum = (int(month) * 9.09091) / 100
    for ys in year_query:
        year += ys.transAmount
        year_sum = (int(year) * 9.09091) / 100
    for ts in total_query:
        total += ts.transAmount
        total_sum = (int(total) * 9.09091) / 100
    data = [{
       'today':str(round(today_sum, 2)),
       'month':str(round(month_sum, 2)),
       'year': str(round(year_sum, 2)),
       'total':str(round(total_sum))
    }]
    return Response(data)


### backoffice mpesa summary

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def mpesaOfficeStat(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    w_date = timezone.now()
    week_date = w_date.strftime("%V")
    month_date = timezone.now().month
    year_date = timezone.now().year
    today = 0
    week = 0
    month = 0
    year = 0
    total = 0
    today_query = MpesaPayment.objects.filter(created__range=[today_start, today_end ] )
    week_query = MpesaPayment.objects.filter(created__week=week_date)
    month_query = MpesaPayment.objects.filter(created__month=month_date)
    year_query = MpesaPayment.objects.filter(created__year=year_date)
    total_query = MpesaPayment.objects.all()

    for tos in today_query:
        today += tos.transAmount
    
    for ws in week_query:
        week += ws.transAmount
   
    for ms in month_query:
        month += ms.transAmount

    for ys in year_query:
        year += ys.transAmount

    for ts in total_query:
        total += ts.transAmount

    data = {
       'today':today,
       'week':week,
       'month':month,
       'year': year,
       'total':total
    }
    return Response(data)


#### MPESA OFFICE FILTERS BY DATE

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_stat_range_total(request):
    post_data = request.data
    today_start = post_data['fromdate']
    today_end = post_data['todate']
    data1 = MpesaPayment.objects.filter(created__range=[today_start, today_end ], billRefNumber='1111' )
    data2 = MpesaPayment.objects.filter(created__range=[today_start, today_end ], billRefNumber='9017' )
    data3 = MpesaPayment.objects.filter(created__range=[today_start, today_end ], billRefNumber='2580' )
    data4 = MpesaPayment.objects.filter(created__range=[today_start, today_end ])
    data_tot_1 = 0
    data_tot_2 = 0
    data_tot_3 = 0
    other_tot_1 = 0
    for ts in data1:
        data_tot_1 += ts.transAmount
    for ts in data2:
        data_tot_2 += ts.transAmount
    for ts in data3:
        data_tot_3 += ts.transAmount
    for ts in data4:
        other_tot_1 += ts.transAmount
    data_tot = data_tot_1 + data_tot_2 + data_tot_3
    other_tot = other_tot_1 - data_tot
    data_resp = {
        'swap':data_tot,
        'total': other_tot_1,
        'others': other_tot,
    }
    return Response(data_resp)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaFilterToday(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    data = MpesaPayment.objects.filter(created__range=[today_start, today_end ] )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaFilterWeek(request):
    w_date = timezone.now()
    week_date = w_date.strftime("%V")
    data = MpesaPayment.objects.filter(created__week=week_date)
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaFilterMonth(request):
    month_date = timezone.now().month
    data = MpesaPayment.objects.filter(created__month=month_date)
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaFilterYear(request):
    year_date = timezone.now().year
    data = MpesaPayment.objects.filter(created__year=year_date)
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaFilterRange(request):
    data = request.data
    today_start = data['fromdate']
    today_end = data['todate']
    data = MpesaPayment.objects.filter(created__range=[today_start, today_end ] )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def mpesa_acc_filter(request):
    qry = request.data
    ref = qry['acc_filter']
    fromdate = qry['fromdate']
    todate = qry['todate']
    if len(fromdate) > 0:
        data = MpesaPayment.objects.filter(created__range=[fromdate, todate ] ).filter(billRefNumber=ref)
        serializer = MpesaSerializer(data, many=True)
    data = MpesaPayment.objects.filter(billRefNumber=ref)
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


#### OFFICE > TRANSACTION

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaList(request):
    data = MpesaPayment.objects.all().order_by('-id')[:50]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesabyid(request,id):
    data = MpesaPayment.objects.get(id=id)
    serializer = MpesaSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaUpdate(request,id):
    feedback_msg = {}
    query = MpesaPayment.objects.get(id=id)
    serializer = MpesaSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaSearch(request, cod):
    data = MpesaPayment.objects.filter( Q(transID=cod) | Q(billRefNumber=cod) | Q(firstName=cod) )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaDelete(request, id):
    feedback_msg = {}
    MpesaPayment.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)

