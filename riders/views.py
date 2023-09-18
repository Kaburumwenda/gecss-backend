from .serializers import *
from .models import *
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
def riders_min_list(request):
    data = Riders.objects.filter(is_delete='0').order_by('-createdAt')[:25]
    serializer = RidersSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riders_list(request):
    data = Riders.objects.filter(is_delete='0').order_by('-createdAt')
    serializer = RidersSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riders_byid(request,id):
    data = Riders.objects.get(id=id)
    serializer = RidersSerializer(data, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riders_update(request,id):
    feedback_msg = {}
    query = Riders.objects.get(id=id)
    serializer = RidersSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riders_search(request, cod):
    data = Riders.objects.filter( Q(user__username=cod) | Q(numberplate=cod) )
    serializer = RidersSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riders_delete(request, id):
    feedback_msg = {}
    Riders.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
class riders_create(APIView):
    def post(self, request):
        try:
            data = request.data
            Riders.objects.create(
                bike_no = data['bike_no'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                middle_name = data['middle_name'],
                gender = data['gender'],
                age = data['age'],
                id_no = data['id_no'],
                id_type = data['id_type'],
                date_registered = data['date_registered'],
                status = data['status'],
                mobile = data['mobile'],
                alt_mobile = data['alt_mobile'],
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)