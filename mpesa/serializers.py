from rest_framework.serializers import ModelSerializer
from .models import *


class MpesaSerializer(ModelSerializer):
    class Meta:
        model = MpesaCipher
        fields = [ 'id', 'client', 'memNo', 'mobile', 'amount', 'checkoutid', 'createdAt', 'updatedAt', 'status']