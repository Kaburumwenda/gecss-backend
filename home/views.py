from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from battery.models import BatterySwap, Battery
from motobikes.models import Motobikes
from iam.models import StaffAccount
from django.db.models.functions import ExtractMonth, ExtractDay
# from django.db.models.functions import TruncMonth, TruncDay
from django.db.models import Avg, Count, Q, F, Sum
from datetime import datetime
from django.db.models import Value as V
from django.db.models.functions import Coalesce
from django.utils import timezone
from mpesa.models import MpesaPayment
# Create your views here.

### TOTALS COUNTS
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def totalsCount(request):
    earnings = 0
    earnings_query = MpesaPayment.objects.all()
    for rs in earnings_query:
        earnings += rs.transAmount
    batteries = Battery.objects.all().count()
    bikes = Motobikes.objects.all().count()
    staff = StaffAccount.objects.all().count()
    data = {
        'earnings':earnings,
        'batteries':batteries,
        'bikes': bikes,
        'staff': staff
    }
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def statisticsGraphs(request):
    this_month = timezone.now().month
    data = MpesaPayment.objects.filter(
        created__month=this_month).annotate(day=ExtractDay('created')).values('day').annotate(
            totals=Sum('transAmount')).values('day', 'totals')

    # data = BatterySwap.objects.filter(
    #     updatedAt__month=this_month).annotate(day=ExtractDay('updatedAt')).values('day').annotate(
    #         totals=Sum('amount')).values('day', 'totals')
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def batteryStation(request):
    data = BatteryStation.objects.all().order_by('-id')
    serializer = BatteryStationSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def companyBranches(request):
    data = GecssBranch.objects.all().order_by('-id')
    serializer = BranchesSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def companyBranchbyid(request, id):
    data = GecssBranch.objects.get(id=id)
    serializer = BranchesSerializer(data, many=False)
    return Response(serializer.data)



#### AGENT NOTIFICATIONS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentNotificationList(request):
    data = AgentNotification.objects.all().order_by('-id')
    serializer = AgentNotificationSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentNotificationbyid(request,id):
    data = AgentNotification.objects.get(id=id)
    serializer = AgentNotificationSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentNotificationUpdate(request,id):
    feedback_msg = {}
    query = AgentNotification.objects.get(id=id)
    serializer = AgentNotificationSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentNotificationSearch(request, cod):
    data = AgentNotification.objects.filter( title__contains=cod )
    serializer = AgentNotificationSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentNotificationDelete(request, id):
    feedback_msg = {}
    AgentNotification.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class AgentNotificationCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            source = data['source']
            title = data['title']
            message = data['message']
            AgentNotification.objects.create(
                source = source,
                title = title,
                message = message
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)
