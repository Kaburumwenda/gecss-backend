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