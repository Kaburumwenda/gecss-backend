from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F

@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userList(request):
    data = User.objects.filter(is_active='True')
    serializer = UserListserializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userData(request, id):
    data = User.objects.get(id=id)
    serializer = UserListserializer(data, many=False)
    return Response(serializer.data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userSearch(request, username):
    data = User.objects.filter(username__icontains=username)
    serializer = UserListserializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userUpdate(request,id):
    feedback_msg = {}
    query = User.objects.get(id=id)
    serializer = UserListserializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def userDelete(request, id):
    feedback_msg = {}
    User.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


######

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffUsernames(request):
    data = []
    data = User.objects.filter(is_staff='True').values_list('username', flat=True)
    return Response(data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffList(request):
    data = User.objects.filter(is_staff='True')
    serializer = UserListserializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffAccounts(request):
    data = StaffAccount.objects.filter(user__is_staff=True)
    serializer = StaffAccountSerializer(data, many=True)
    return Response(serializer.data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffAccountbyid(request, id):
    data = StaffAccount.objects.get(id=id)
    serializer = StaffAccountSerializer(data, many=False)
    return Response(serializer.data)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffSearch(request, cod):
    data = StaffAccount.objects.filter( Q(user__username=cod ) | Q ( phone=cod ) | Q(idNo=cod) )
    serializer = StaffAccountSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffUpdate(request,id):
    feedback_msg = {}
    query = StaffAccount.objects.get(id=id)
    serializer = StaffAccountSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class StaffAccountCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            idNo = data['idNo']
            department = data['department']
            designation = data['designation']
            phone = data['phone']
            alt_phone = data['alt_phone']
            sex = data['sex']
            age = data['age']
            operation_area = data['operation_area']
            user = User.objects.get(username=data['username'])
            StaffAccount.objects.create(
                user = user,
                idNo = idNo,
                designation = designation,
                department = department,
                phone = phone,
                alt_phone = alt_phone,
                sex = sex,
                age = age,
                operation_area = operation_area
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def staffAccountDelete(request, id):
    feedback_msg = {}
    StaffAccount.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)