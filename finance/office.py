from django.shortcuts import render
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userAccountList(request):
    data = userAccount.objects.all()
    serializer = userAccountSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userAccountbyid(request,id):
    data = userAccount.objects.get(id=id)
    serializer = userAccountSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userAccountUpdate(request,id):
    feedback_msg = {}
    query = userAccount.objects.get(id=id)
    serializer = userAccountSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userAccountSearch(request, username):
    data = userAccount.objects.filter(user__username=username)
    serializer = userAccountSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userAccountDelete(request, id):
    feedback_msg = {}
    userAccount.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)

class UserAccountCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            idNo = data['idNo']
            phone = data['phone']
            alt_phone = data['alt_phone']
            sex = data['sex']
            age = data['age']
            occupation = data['occupation']
            residential = data['residential']
            operation_area = data['operation_area']
            bikes = data['bikes']
            amount = data['amount']
            balance = data['balance']
            userdet = data['username']
            user = User.objects.get(username=userdet)
            userAccount.objects.create(
                user = user,
                idNo = idNo,
                phone = phone,
                alt_phone = alt_phone,
                sex = sex,
                age = age,
                occupation = occupation,
                residential = residential,
                operation_area = operation_area,
                bikes = bikes,
                amount = amount,
                balance = balance,      
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)



#### OFFICE > TRANSACTION

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def transactionList(request):
    data = Transaction.objects.all().order_by('-id')[:50]
    serializer = TransactionSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def transactionbyid(request,id):
    data = Transaction.objects.get(id=id)
    serializer = TransactionSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def transactionUpdate(request,id):
    feedback_msg = {}
    query = Transaction.objects.get(id=id)
    serializer = TransactionSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def transactionSearch(request, cod):
    data = Transaction.objects.filter(user__username=cod )
    serializer = TransactionSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def transactionDelete(request, id):
    feedback_msg = {}
    Transaction.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)



class TransactionCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            purpose = data['purpose']
            amount = data['amount']
            status = data['status']
            userdet = data['memNo']
            user = User.objects.get(username=userdet)
            Transaction.objects.create(
                user = user, 
                purpose = purpose,
                amount = amount,
                status = status   
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)
