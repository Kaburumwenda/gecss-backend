from rest_framework.serializers import ModelSerializer
from .models import *


class MpesaSerializer(ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields = [ 
            'id', 'transactionType', 'transID', 'transTime', 'firstName',
            'transAmount','billRefNumber','orgAccountBalance', 'agentCommission', 'MSISDN', 'created'
            ]