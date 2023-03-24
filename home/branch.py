from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F
# Create your views here.


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication ])
# def companyBranches(request):
#     data = GecssBranch.objects.all().order_by('-id')
#     serializer = BranchesSerializer(data, many=True)
#     return Response(serializer.data)


class CompanyBranch(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get(self, request):
        data = GecssBranch.objects.all().order_by('-id')
        serializer =  BranchesSerializer(data, many=True)
        
        return Response(serializer.data) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def branchList(request):
    data = []
    data = GecssBranch.objects.values_list('title', flat=True)
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def branchList(request):
    data = []
    data = GecssBranch.objects.values_list('title', flat=True)
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def companyBranchbyid(request, id):
    data = GecssBranch.objects.get(id=id)
    serializer = BranchesSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def branchUpdate(request,id):
    feedback_msg = {}
    query = GecssBranch.objects.get(id=id)
    serializer = BranchesSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def branchSearch(request, cod):
    data = GecssBranch.objects.filter( Q(code=cod) | Q(title=cod) )
    serializer = BranchesSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def branchDelete(request, id):
    feedback_msg = {}
    GecssBranch.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class BranchCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            code = data['code']
            status = data['status']
            title = data['title']
            GecssBranch.objects.create(
                code = code,
                title = title,
                status = status,
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)