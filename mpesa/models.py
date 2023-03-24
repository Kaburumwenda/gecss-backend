from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()

# Create your models here.
class MpesaCipher(models.Model):
    user = models.ForeignKey(User, on_delete=models.Case)
    mobile = models.CharField(max_length=150)
    amount = models.PositiveIntegerField(default=1)
    checkoutid = models.CharField(max_length=150)
    status = models.CharField(max_length=20, default='Paid')
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.checkoutid

    def memNo(self):
        return self.user.username
        
    def client(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class MpesaPayment(models.Model):
    transactionType = models.CharField(max_length=50)
    transID = models.CharField(max_length=50)
    transTime = models.CharField(max_length=50)
    transAmount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    billRefNumber = models.CharField(max_length=50)
    orgAccountBalance = models.CharField(max_length=50)
    MSISDN = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName

    def agentCommission(self):
        am = int(self.transAmount)
        am_fe = (am * 9.09091) / 100
        am_f = round(am_fe, 2)
        return f"{am_f}"


class MpesaPay(models.Model):
    transactionType = models.CharField(max_length=50)
    transID = models.CharField(max_length=50)
    transTime = models.CharField(max_length=50)
    transAmount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    billRefNumber = models.CharField(max_length=50)
    orgAccountBalance = models.CharField(max_length=50)
    MSISDN = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName
        
    def agentCommission(self):
        am = int(self.transAmount)
        am_fe = (am * 9.09091) / 100
        am_f = round(am_fe, 2)
        return f"{am_f}"