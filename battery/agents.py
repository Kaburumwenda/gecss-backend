from .serializers import *
from .models import *
from iam.models import StaffAccount
from motobikes.models import Motobikes
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F


##### ISSUE BATTERY
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agents_batteries(request):
    user = request.user
    # check staff/agent location
    loc = StaffAccount.objects.get(user=user)
    agent_location = loc.operation_area 
    battery_charged = Battery.objects.filter(location=agent_location, status='Charged').count()
    battery_depleted = BatterySwap.objects.filter(mem_no=user, status='Depleted').count()
    battery_issued = Battery.objects.filter(location=agent_location, status='Issued').count()
    data = {
        'charged':battery_charged,
        'depleted':battery_depleted,
        'issued': battery_issued
    }
    return Response(data)


class BatteryAgentsSwapCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            user = request.user
            data = request.data
            # check staff/agent location
            loc = StaffAccount.objects.get(user=user)
            location = loc.operation_area 
            amount = '150'
            bike_no = data['bike_no']
            battery_code1 = data['battery_code1']
            ### UPDATE BATTERY RECORD TO ISSUED
            query = Battery.objects.get(code=battery_code1)
            bat_status = query.status
            query.status = 'Issued'
            query.save(update_fields=["status"]) 
            ### CREATE BATTERY SWAP RECORD
            BatterySwap.objects.create(
                mem_no = user,
                bike_no = bike_no,
                battery_code1 = battery_code1,
                amount = amount,
                source = location,
            )
            response_msg = {"error": "0", "message": "Battery issued succeccfully"}
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)


##### RETAKE BATTERY

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def checkbike(request):
    data = request.data
    try:
       swap_record = BatterySwap.objects.filter(battery_code1=data['battery_code'], status='Issued')[0]
       bike = swap_record.bike_no
       response_msg = {"error": "0", "message": "BIKE NO: {} : Please ensure bike number plate is as indicated".format(bike) }
    except:
       response_msg = {"error": "1", "message": "Battery record not found in database. Please consult sys Admin"}
    return Response(response_msg)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def retakeBattery(request):
    data = request.data
    try:
       
       response_msg = {"error": "0", "message": "BIKE NO: {} : Please ensure bike number plate is as indicated".format(bike) }
    except:
       response_msg = {"error": "1", "message": "Battery record not found in database. Please consult sys Admin"}
    return Response(response_msg)



class BatteryAgentsRetake(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            user = request.user
            data = request.data
            # check staff/agent location
            # loc = StaffAccount.objects.get(user=user)
            # location = loc.operation_area 
            # amount = '150'
            # status = 'Depleted'
            battery_code1 = data['battery_code']
            ### bike number
            # swap_record = BatterySwap.objects.filter(battery_code1=data['battery_code'], status='Issued')[0]
            # bike = swap_record.bike_no
            # bike_no = bike
            ### UPDATE BATTERY RECORD TO ISSUED
            query = Battery.objects.get(code=battery_code1)
            query.status = 'Depleted'
            query.save(update_fields=["status"]) 
            ### CREATE BATTERY SWAP RECORD
            query = BatterySwap.objects.filter(battery_code1=battery_code1, status='Issued')[0]
            query.status = 'Depleted'
            query.save(update_fields=["status"]) 
           
            response_msg = {"error": "0", "message": "Battery issued succeccfully"}
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)