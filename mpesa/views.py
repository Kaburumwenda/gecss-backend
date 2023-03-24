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
        "AccountReference": phone,
        "TransactionDesc": "GECSS INVESTMENT"
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesa_cipher(request):
    data = request.data
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
    return Response(resp)


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://aws.gecss.v3engine.gecss-ke.com/v1/c2b/confirmation",
               "ValidationURL": "https://aws.gecss.v3engine.gecss-ke.com/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)


@csrf_exempt
@require_POST
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    MpesaPayment.objects.create(
         firstName=mpesa_payment['FirstName'],
         transID=mpesa_payment['TransID'],
         MSISDN=mpesa_payment['MSISDN'],
         transTime=mpesa_payment['TransTime'],
         transAmount=mpesa_payment['TransAmount'],
         billRefNumber=mpesa_payment['BillRefNumber'],
         orgAccountBalance=mpesa_payment['OrgAccountBalance'],
         transactionType=mpesa_payment['TransactionType'],
    )
    response='Success'
    return HttpResponse(response)
