from rest_framework.serializers import ModelSerializer

from .models import *

class RidersSerializer(ModelSerializer):
    class Meta:
        model = Riders
        fields = ['rider_id', 'bike_no', 'first_name', 'last_name', 'middle_name', 'mobile', 'alt_mobile',
                 'gender', 'age', 'ID_document_number', 'ID_document_type', 'status', 'date_registered', 'createdAt', 'updatedAt']