from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
import requests
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.csrf import csrf_exempt
from .mpesa_creditials import MpesaAccessToken, LipanaMpesaPpassword 
from django.views.decorators.http import require_POST
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from time import sleep
from .models import *
from finance.models import Transaction, userAccount
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.
	

def getAccessToken(request):
    consumer_key = 'En5W08NAEaGrlCSA1S4UZkTkAA4UH5gG'
    consumer_secret = 'zqU1ud4AjBQLpAh7'
    # api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def lipa_na_mpesa_online(request):
    data = request.data
    phone = data['phone']
    tel = phone[1:]
    tel_a = '254'
    tel_b = tel_a + tel
    phone_number = int(tel_b)
    amount = int(data['amount'])

    consumer_key = 'En5W08NAEaGrlCSA1S4UZkTkAA4UH5gG'
    consumer_secret = 'zqU1ud4AjBQLpAh7'
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL,
                     auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    access_token = mpesa_access_token['access_token']
 
    # access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,  
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://yummy-peaches-retire-197-232-147-3.loca.lt/mpesa/confirmation",
        "AccountReference": "GECSS INVESTMENT",
        "TransactionDesc": "GECSS INVESTMENT"
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_cipher(request):
    user_id = request.user
    data = request.data
    resp_msg = {}
    # sleep(10)
    consumer_key = 'En5W08NAEaGrlCSA1S4UZkTkAA4UH5gG'
    consumer_secret = 'zqU1ud4AjBQLpAh7'
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL,
                     auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    access_token = mpesa_access_token['access_token']

    api_url = "https://api.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "CheckoutRequestID":data['checkoutid']
    }
    resp = requests.post(api_url, json=request, headers=headers)
    resp1 = resp.text
    resp2 = json.loads(resp1)
    result_code = resp2.get('ResultCode')
    result_msg = resp2.get('ResultDesc')
    if result_code == '0':
        user = User.objects.get(username=user_id)
        amount = data['amount']
        mobile = data['mobile']
        checkoutid = data['checkoutid']
        #### CREATING NEW MPESA TRANSACTION RECORD
        MpesaCipher.objects.create(
            user = user,
            mobile = mobile,
            amount = amount,
            checkoutid = checkoutid,
        )
        #### CREATING NEW TRANSACTIONS
        Transaction.objects.create(
            user = user,
            amount = amount,
        )
        ### UPDATING USER BALANCE
        query = userAccount.objects.get(user=user)
        initial_bal = query.balance
        recur_bal = initial_bal - int(amount)
        query.balance = recur_bal
        query.save(update_fields=["balance"]) 
        resp_msg = {
            "error":"0",
            "success": result_msg
        }
    if result_code != '0':
        resp_msg = {
            "error":"1",
            "success": result_msg
        }
    return Response(resp_msg)


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://gecss-ke.com/api/v1/c2b/confirmation",
               "ValidationURL": "https://gecss-ke.com/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)



@csrf_exempt
@require_POST
def confirmation(request):
    print('Hello Mwenda')
    stk ={}
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    stk = mpesa_payment.get("Body")
    stk_callback = stk.get("stkCallback")
    result_code = stk_callback.get("ResultCode")
    result_desc = stk_callback.get("ResultDesc")
    print('############################') # 'ResultCode': 1032, 'ResultDesc':
    print(result_desc)
    print(result_code)
    print(mpesa_payment)

    # mpesa_body =request.body.decode('utf-8')
    # mpesa_payment = json.loads(mpesa_body)
    # print(mpesa_payment)
    # payment = MpesaPayment(
    #     first_name=mpesa_payment['FirstName'],
    #     last_name=mpesa_payment['LastName'],
    #     middle_name=mpesa_payment['MiddleName'],
    #     description=mpesa_payment['TransID'],
    #     phone_number=mpesa_payment['MSISDN'],
    #     amount=mpesa_payment['TransAmount'],
    #     reference=mpesa_payment['BillRefNumber'],
    #     organization_balance=mpesa_payment['OrgAccountBalance'],
    #     type=mpesa_payment['TransactionType'],

    # )
    # payment.save()

    # context = {
    #     "ResultCode": 0,
    #     "ResultDesc": "Accepted"
    #
    response='Hello Kaburu'
    return HttpResponse(response)

    # return JsonResponse(dict(context))
