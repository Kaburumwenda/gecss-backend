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
def agentPaymentList(request):
    agent = request.user
    data = AgentPayment.objects.filter(agentNo=agent).order_by('-id')
    serializer = AgentPaymentSerializer(data, many=True)
    return Response(serializer.data)