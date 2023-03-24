from rest_framework.serializers import ModelSerializer

from .models import *

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [ 'id', 'client', 'memNo', 'purpose', 'amount', 'status', 'createdAt', 'updatedAt']


class userAccountSerializer(ModelSerializer):
    class Meta:
        model = userAccount
        fields = [ 
            'id','client', 'memNo', 'bikes', 'idNo','phone','alt_phone','sex','age','occupation',
            'residential','operation_area','amount','balance','createdAt','updatedAt'
        ]


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = [ 'id', 'item', 'quantity', 'units_conversion', 'price',
                 'approvedby','department', 'date', 'status', 'createdAt']