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


@api_view(['GET'])
def trendslist(request):
    data = CompanyTrend.objects.filter(status='Active').order_by('?')
    serializer = CompanyTrendSerializer(data, many=True)
    return Response(serializer.data)


# class CompanyBranch(APIView):
#     def get(self, request):
#         data = GecssBranch.objects.all().order_by('-id')
#         serializer =  BranchesSerializer(data, many=True)
        
#         return Response(serializer.data) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def trendsbyid(request, id):
    data = CompanyTrend.objects.get(id=id)
    serializer = CompanyTrendSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def trendsUpdate(request,id):
    feedback_msg = {}
    query = CompanyTrend.objects.get(id=id)
    serializer = CompanyTrendSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def trendsSearch(request, cod):
    data = CompanyTrend.objects.filter( title=cod )
    serializer = CompanyTrendSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def trendsDelete(request, id):
    feedback_msg = {}
    CompanyTrend.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class TrendsCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            title = data['title']
            desc = data['desc']
            status = data['status']
            imgurl = data['imgurl']
            CompanyTrend.objects.create(
                title = title,
                desc = desc,
                status = status,
                imgurl = imgurl
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)