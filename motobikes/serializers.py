from rest_framework.serializers import ModelSerializer

from .models import *

class MotobikeSerializer(ModelSerializer):
    class Meta:
        model = Motobikes
        fields = [ 'id', 'memNo', 'numberplate', 'client', 'status', 'condition', 'createdAt', 'updatedAt']