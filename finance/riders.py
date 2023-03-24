from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def riderTransaction(request):
    user = request.user
    data = Transaction.objects.filter(user=user).order_by('-id')[:2]
    serializer = TransactionSerializer(data, many=True)
    return Response(serializer.data)