from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes


class RegisterView(APIView):
    def post(self, request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors,)

# Create your views here.

@api_view(['GET'])
def userNotification(request):
    data = Notifications.objects.filter(status='Active').order_by('-id')
    serializer = NotificationSerializer(data, many=True)
    return Response(serializer.data)


def userList(request):
    data = User.objects.filter(status='Active').order_by('-id')
    serializer = Userlistserializer(data, many=True)
    return Response(serializer.data)


