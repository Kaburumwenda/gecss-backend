from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notifications(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=550)
    status = models.CharField(max_length=30, choices=STATUS, default='Active')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StaffAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.Case)
    idNo = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    alt_phone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    operation_area = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Active')
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.idNo

    def username(self):
        return self.user.username
        
    def staff(self):
        return f"{self.user.first_name}  {self.user.last_name}"