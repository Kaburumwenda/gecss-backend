from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(('GET',))
def userList(request):
    data = User.objects.filter(is_active='True')
    serializer = UserListserializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def userData(request, id):
    data = User.objects.get(id=id)
    serializer = UserListserializer(data, many=False)
    return Response(serializer.data)


@api_view(('GET',))
def userSearch(request, username):
    data = User.objects.filter(username__icontains=username)
    serializer = UserListserializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request,id):
    feedback_msg = {}
    query = User.objects.get(id=id)
    serializer = UserListserializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(['DELETE'])
def userDelete(request, id):
    feedback_msg = {}
    User.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)