from rest_framework import serializers
from .models import *


class AgentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPayment
        fields = ['id', 'agentNo', 'amount', 'status', 'fromDate', 'toDate','createdAt' ]