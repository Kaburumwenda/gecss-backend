import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'En5W08NAEaGrlCSA1S4UZkTkAA4UH5gG'
    consumer_secret = 'zqU1ud4AjBQLpAh7'
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "4093687"
    Test_c2b_shortcode = "4093687"
    passkey = '281bc9ef53f443ce3abcfb76af1b755dcebde7b1e511d2c4362578d22736e91c'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

 #USERNAME ==> skyman
# pass ==> Rahma1900
#email ==> yuskaburu

#https://github.com/martinmogusu/django-daraja
#https://blog.hlab.tech/lesson-3-a-step-by-step-tutorial-on-how-to-do-stk-push-integration-to-m-pesa-on-daraja-using-django-2-2-and-python-3-7/
#https://github.com/HenryLab/Python-Django-Mpesa-API-Integration
