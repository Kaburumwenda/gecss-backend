from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = ['id', 'code', 'location', 'status', 'condition' ]


class BatteryStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryStation
        fields = ['id', 'title', 'head', 'phone', 'status' ]


class BatterySwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatterySwap
        fields = ['id', 'bike_no', 'mem_no', 'battery_code1', 'amount', 'source', 'status', 'createdAt', 'updatedAt' ]