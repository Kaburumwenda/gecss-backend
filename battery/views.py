from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F


@api_view(['GET'])
def batteries(request):
    data = Battery.objects.all().order_by('-id')
    serializer = BatterySerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
def batterybyid(request,id):
    data = Battery.objects.get(id=id)
    serializer = BatterySerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def batteryUpdate(request,id):
    feedback_msg = {}
    query = Battery.objects.get(id=id)
    serializer = BatterySerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)
    
@api_view(('GET',))
def batterySearch(request, cod):
    data = Battery.objects.filter(code__icontains=cod)
    serializer = BatterySerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def batteryDelete(request, id):
    feedback_msg = {}
    Battery.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class BatteryCreate(APIView):
    def post(self, request):
        try:
            data = request.data
            code = data['code']
            location = data['location']
            status = data['status']
            condition = data['condition']
            Battery.objects.create(
                code = code,
                location = location,
                status = status,
                condition = condition,  
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)


##### BATTERY STATIONS

@api_view(['GET'])
def batteryStations(request):
    data = BatteryStation.objects.all().order_by('-id')
    serializer = BatteryStationSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def batteryStationbyid(request,id):
    data = BatteryStation.objects.get(id=id)
    serializer = BatteryStationSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def batteryStationUpdate(request,id):
    feedback_msg = {}
    query = BatteryStation.objects.get(id=id)
    serializer = BatteryStationSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
def batteryStationSearch(request, cod):
    data = BatteryStation.objects.filter(title__icontains=cod)
    serializer = BatteryStationSerializer(data, many=True)
    return Response(serializer.data)


class BatteryStationCreate(APIView):
    def post(self, request):
        try:
            data = request.data
            title = data['title']
            head = data['head']
            status = data['status']
            phone = data['phone']
            BatteryStation.objects.create(
                title = title,
                head = head,
                status=status,
                phone = phone,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)


@api_view(['DELETE'])
def batterystationDelete(request, id):
    feedback_msg = {}
    BatteryStation.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


#### BATTERY SWAP

@api_view(['GET'])
def batterySwap(request):
    data = BatterySwap.objects.all().order_by('-id')
    serializer = BatterySwapSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def batterySwapbyid(request,id):
    data = BatterySwap.objects.get(id=id)
    serializer = BatterySwapSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def batterySwapUpdate(request,id):
    feedback_msg = {}
    query = BatterySwap.objects.get(id=id)
    serializer = BatterySwapSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class BatterySwapCreate(APIView):
    def post(self, request):
        try:
            data = request.data
            amount = 150
            mem_no = data['mem_no']
            bike_no = data['bike_no']
            battery_code1 = data['battery_code1']
            BatterySwap.objects.create(
                mem_no = mem_no,
                bike_no = bike_no,
                battery_code1 = battery_code1,
                amount = amount,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)

 
@api_view(('GET',))
def batterySwapSearch(request, cod):
    data = BatterySwap.objects.filter(Q(mem_no__icontains=cod) | Q(battery_code1__icontains=cod) | Q(bike_no__icontains=cod) )
    serializer = BatterySwapSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def batterySwapDelete(request, id):
    feedback_msg = {}
    BatterySwap.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)