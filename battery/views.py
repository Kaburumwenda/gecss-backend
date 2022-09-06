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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteries(request):
    data = Battery.objects.all().order_by('-id')
    serializer = BatterySerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterybyid(request,id):
    data = Battery.objects.get(id=id)
    serializer = BatterySerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryUpdate(request,id):
    feedback_msg = {}
    query = Battery.objects.get(id=id)
    serializer = BatterySerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)
    

@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySearch(request, cod):
    data = Battery.objects.filter(code__icontains=cod)
    serializer = BatterySerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryDelete(request, id):
    feedback_msg = {}
    Battery.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class BatteryCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
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
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryStations(request):
    data = BatteryStation.objects.all().order_by('-id')
    serializer = BatteryStationSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryStationbyid(request,id):
    data = BatteryStation.objects.get(id=id)
    serializer = BatteryStationSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryStationUpdate(request,id):
    feedback_msg = {}
    query = BatteryStation.objects.get(id=id)
    serializer = BatteryStationSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batteryStationSearch(request, cod):
    data = BatteryStation.objects.filter(title__icontains=cod)
    serializer = BatteryStationSerializer(data, many=True)
    return Response(serializer.data)


class BatteryStationCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
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
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterystationDelete(request, id):
    feedback_msg = {}
    BatteryStation.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


#### BATTERY SWAP

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySwap(request):
    data = BatterySwap.objects.all().order_by('-id')
    serializer = BatterySwapSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySwapbyid(request,id):
    data = BatterySwap.objects.get(id=id)
    serializer = BatterySwapSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySwapUpdate(request,id):
    feedback_msg = {}
    apiData=request.data
    #battery = Battery.objects.filter( Q(code=apiData['battery_code1']) & ( Q(status='Charging') | Q(status='Charged') ) ).order_by('-id')[:1]
    battery = Battery.objects.filter( code=apiData['battery_code1'] ).order_by('-id')[:1]
    battery_id = battery[0].id
    if battery_id < 0:
        feedback_msg = { 'error':'true' }
    battery_query = Battery.objects.get(id=battery_id)
    query_swap = BatterySwap.objects.get(id=id)
    battery_data = {
        'status':apiData['status']
    }
    serializer = BatterySerializer(instance=battery_query, data=battery_data, partial=True)
    serializer_swap = BatterySwapSerializer(instance=query_swap, data=request.data, partial=True)
    if serializer.is_valid() & serializer_swap.is_valid():
         serializer_swap.save()
         serializer.save()
         feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class BatterySwapCreate(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            user = request.user
            data = request.data
            # check staff/agent location
            loc = StaffAccount.objects.get(user=user)
            location = loc.operation_area 
            # check staff/agent username/member
            mem_no = ''
            mem = Motobikes.objects.filter(numberplate=data['bike_no'])
            if mem.count() < 0:
                response_msg = {"error": True, "message": "Motorbike number plate not found !"}
            mem_no = mem[0].user
            amount = '150'
            bike_no = data['bike_no']
            battery_code1 = data['battery_code1']
            BatterySwap.objects.create(
                mem_no = mem_no,
                bike_no = bike_no,
                battery_code1 = battery_code1,
                amount = amount,
                source = location,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)

 
@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySwapSearch(request, cod):
    data = BatterySwap.objects.filter(Q(mem_no__icontains=cod) | Q(battery_code1__icontains=cod) | Q(bike_no__icontains=cod) )
    serializer = BatterySwapSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def batterySwapDelete(request, id):
    feedback_msg = {}
    BatterySwap.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)