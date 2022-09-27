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
# Create your views here.

#### OFFICE > TRANSACTION

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaList(request):
    data = MpesaCipher.objects.all().order_by('-id')[:50]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesabyid(request,id):
    data = MpesaCipher.objects.get(id=id)
    serializer = MpesaSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaUpdate(request,id):
    feedback_msg = {}
    query = MpesaCipher.objects.get(id=id)
    serializer = MpesaSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaSearch(request, cod):
    data = MpesaCipher.objects.filter( Q(user__username=cod) | Q(mobile=cod) )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaDelete(request, id):
    feedback_msg = {}
    MpesaCipher.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)

