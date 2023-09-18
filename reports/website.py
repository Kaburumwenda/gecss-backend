from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F, Sum
from django.db.models.functions import ExtractMonth, ExtractDay

from battery.models import Battery, BatterySwap, BatteryStation
from motobikes.models import Motobikes
from battery.serializers import BatterySwapSerializer

from datetime import datetime, timedelta, time
from django.utils import timezone

#bike_no
@api_view(['GET'])
def website_report(request):
    data = {}
    swaps = 0
    mileage =0
    carbon = 0
    data_qry = BatterySwap.objects.all().count()
    swaps = data_qry
    mileage = data_qry * 95
    carbon = data_qry * 8.64

    data = {
        "swaps": swaps,
        "mileage": mileage,
        "carbon": carbon,
    }
    return Response(data)