from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *

class BatteryStationSerializer(ModelSerializer):
    class Meta:
        model = BatteryStation
        fields = ['location','description','charged_battery', 'discharged_battery','date', 'getImage']


class BranchesSerializer(ModelSerializer):
    class Meta:
        model = GecssBranch
        fields = ['title', 'code', 'status', 'id']


class AgentNotificationSerializer(ModelSerializer):
    class Meta:
        model = AgentNotification
        fields = [ 'id', 'title', 'source', 'message', 'date', 'status']


class CompanyTrendSerializer(ModelSerializer):
    class Meta:
        model = CompanyTrend
        fields = [ 'id', 'title', 'status', 'date',  'imgurl', 'Imgsrc', 'desc']