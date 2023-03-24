from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F


class BatteryAssign(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            data = request.data
            battery_code1 = data['batteryCode']
            branch = data['branch']
    
            query = Battery.objects.get(code=battery_code1)
            query.location = branch
            query.save(update_fields=["location"])
            ### CREATE BATTERY SWAP RECORD
           
            response_msg = {"error": "0", "message": "Battery Assigned to {} succeccfully".format(branch) }
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)


class BatteryCharging(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            data = request.data
            battery_code1 = data['batteryCode']
            branch = data['branch']
    
            query = Battery.objects.get(code=battery_code1)
            query.location = branch
            query.status = 'Charging'
            query.save(update_fields=["location", "status"])
            ### CREATE BATTERY SWAP RECORD
           
            response_msg = {"error": "0", "message": "Battery status updated to Charging succeccfully" }
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)


class BatteryCharged(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            data = request.data
            battery_code1 = data['batteryCode']
            branch = data['branch']
    
            query = Battery.objects.get(code=battery_code1)
            query.location = branch
            query.status = 'Charged'
            query.save(update_fields=["location", "status"])
            ### CREATE BATTERY SWAP RECORD
           
            response_msg = {"error": "0", "message": "Battery status updated to Charged succeccfully" }
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryBranchStatistics(request):
    data = request.data
    loc = data['loc']
    batteries = Battery.objects.filter(location=loc).count()
    issued = Battery.objects.filter(location=loc, status='Issued').count()
    depleted = Battery.objects.filter(location=loc, status='Depleted').count()
    charging = Battery.objects.filter(location=loc, status='Charging').count()
    charged = Battery.objects.filter(location=loc, status='Charged').count()
    data = {
        'batteries':batteries,
        'issued': issued,
        'depleted': depleted,
        'charging': charging,
        'charged': charged
    }
    return Response(data)