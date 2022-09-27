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

@api_view(['POST'])
def etr_test(request):
    invoice_no = ''
    resp_msg ={}
    data = request.data
    inv = data['InvoiceNumber']

    if(inv > 0):
        invoice_no = inv
        resp_msg = {
            "ResultCode":"0",
            "Success":"True",
            "CustomerMessage":"Invoice number {} received".format(invoice_no),
        }
    elif(inv <= 0):
        resp_msg = {
            "ResultCode":"403",
            "Success":"False",
            "CustomerMessage":"Oops !!!. server failed to process your request. Invalid entity. Please try again later",
        }
    else:
        resp_msg = {
            "ResultCode":"503",
            "Success":"False",
            "CustomerMessage":"Oops !!!. server failed to process your request. Invalid entity. Please try again later",
        }

    return Response(resp_msg)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def motorbikeList(request):
    data = Motobikes.objects.all()
    serializer = MotobikeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def motorbikebyid(request,id):
    data = Motobikes.objects.get(id=id)
    serializer = MotobikeSerializer(data, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def motorbikeUpdate(request,id):
    feedback_msg = {}
    query = Motobikes.objects.get(id=id)
    serializer = MotobikeSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def motorbikeSearch(request, cod):
    data = Motobikes.objects.filter( Q(user__username=cod) | Q(numberplate=cod) )
    serializer = MotobikeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def motorbikeDelete(request, id):
    feedback_msg = {}
    Motobikes.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class MotorbikeCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            numberplate = data['numberplate']
            status = data['status']
            condition = data['condition']
            userdet = data['memNo']
            member = User.objects.filter(username=userdet).count()
            if member < 1 :
                response_msg = {"error": True, "message": "Member number not found"}
            user = User.objects.get(username=userdet)
            Motobikes.objects.create(
                user = user,
                numberplate = numberplate, 
                status = status,
                condition = condition,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)