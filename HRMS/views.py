from .serializers import *
from .models import *
from iam.models import StaffAccount
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F
from datetime import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentPayment(request):
    data = AgentPayment.objects.all().order_by('-id')
    serializer = AgentPaymentSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentPaymentbyid(request,id):
    data = AgentPayment.objects.get(id=id)
    serializer = AgentPaymentSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentPaymentUpdate(request,id):
    feedback_msg = {}
    query = AgentPayment.objects.get(id=id)
    serializer = AgentPaymentSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)
    

@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentPaymentSearch(request, cod):
    data = AgentPayment.objects.filter(code__icontains=cod)
    serializer = AgentPaymentSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def agentPaymentDelete(request, id):
    feedback_msg = {}
    AgentPayment.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class AgentPaymentCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            agentNo = data['agentNo']
            amount = data['amount']
            toDate = data['toDate']
            fromDate = data['fromDate']
            AgentPayment.objects.create(
                agentNo = agentNo,
                amount = amount,
                fromDate = fromDate,
                toDate = toDate,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)

