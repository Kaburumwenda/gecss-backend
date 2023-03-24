from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    PURPOSE = (
        ('Daily Deposit', 'Daily Deposit'),
        ('Swap Battery', 'Swap Battery'),
    )
    STATUS = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending','Pending'),
        ('Processing', 'Processing'),
        ('Rejected', 'Rejected'),
        ('Flag', 'Flag'),
    )
    user = models.ForeignKey(User, on_delete=models.Case)
    purpose = models.CharField(max_length=50, choices=PURPOSE, default='Daily Deposit')
    amount = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS, default='Paid')
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def memNo(self):
        return self.user.username
        
    def client(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class userAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.Case)
    idNo = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    alt_phone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    residential = models.CharField(max_length=255)
    operation_area = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=0)
    bikes = models.PositiveIntegerField(default=1)
    balance = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def memNo(self):
        return self.user.username
        
    def client(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class Expense(models.Model):
    item = models.CharField(max_length=555)
    quantity = models.CharField(default=1, max_length=18)
    units_conversion = models.CharField(blank=True, default='None', max_length=50)
    price = models.PositiveIntegerField(default=1)
    approvedby = models.CharField(max_length=255)
    department = models.CharField(max_length=255, default='Office')
    status = models.CharField(max_length=155)
    date = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item