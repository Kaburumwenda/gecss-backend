
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expenseList(request):
    data = Expense.objects.all()
    serializer = ExpenseSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expenseStatistics(request):
    paid = 0
    unpaid = 0
    cancelled = 0
    total = 0
    paid_data = Expense.objects.filter(status='Paid')
    unpaid_data = Expense.objects.filter(status='unPaid')
    cancelled_data = Expense.objects.filter(status='Cancelled')
    total_data = Expense.objects.all()
    for pd in paid_data:
        paid += pd.price
    for ud in unpaid_data:
        unpaid += ud.price
    for cd in cancelled_data:
        cancelled += cd.price
    for td in total_data:
        total += td.price
    data = {
        'paid':paid,
        'unpaid':unpaid,
        'cancelled': cancelled,
        'total': total
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expensebyid(request,id):
    data = Expense.objects.get(id=id)
    serializer = ExpenseSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expenseUpdate(request,id):
    feedback_msg = {}
    query = Expense.objects.get(id=id)
    serializer = ExpenseSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expenseSearch(request, cod):
    data = Expense.objects.filter(item=cod)
    serializer = ExpenseSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def expenseDelete(request, id):
    feedback_msg = {}
    Expense.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


class ExpenseCancel(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request):
        try:
            data = request.data
            getid = data['id']
    
            query = Expense.objects.get(id=getid)
            query.status = 'Cancelled'
            query.save(update_fields=["status"]) 
            ### CREATE BATTERY SWAP RECORD
           
            response_msg = {"error": "0", "message": "Bill or expense cancelled successfully"}
        except:
            response_msg = {"error": "1", "message": "Something is Wrong !. Ensure you have internet connection"}
        return Response(response_msg)


class ExpenseCreate(APIView):
    @permission_classes([IsAuthenticated])
    @authentication_classes([TokenAuthentication ])
    def post(self, request):
        try:
            data = request.data
            item = data['item']
            quantity =data['quantity']
            units_conversion = data['units_conversion']
            approvedby = data['approvedby']
            department = data['department']
            status = data['status']
            price = data['price']
            date = data['date']
            Expense.objects.create(
                item = item, 
                quantity = quantity, 
                units_conversion = units_conversion,
                price = price,
                approvedby = approvedby,
                department = department,
                status = status,
                date = date
            )
            response_msg = {"error": False, "message": "Your work has been saved succeccfully"}
        except:
            response_msg = {"error": True, "message": "Somthing is Wrong !"}
        return Response(response_msg)

