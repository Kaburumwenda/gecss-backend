from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class Userlistserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name','is_active', 'is_staff' )


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notifications
        fields = [ 'title', 'message']


####### OFFICE
class UserListserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',
                  'first_name', 'last_name', 'email', 'date_joined', 'is_active', 'is_staff', 'password')


class StaffAccountSerializer(ModelSerializer):
    class Meta:
        model = StaffAccount
        fields = [ 
            'id','staff', 'username','idNo','phone','alt_phone', 'designation', 'department', 'sex','age',
            'operation_area', 'status','createdAt','updatedAt'
        ]