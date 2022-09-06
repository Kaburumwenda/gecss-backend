from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Motobikes(models.Model):
    STATUS = (
        ('Leased', 'Leased'),
        ('Sold', 'Sold'),
        ('Gecss', 'Gecss')
    )
    CONDITION = (
        ('New', 'New'),
        ('Retrofitted', 'Retrofitted')
    )
    user = models.ForeignKey(User, on_delete=models.Case)
    numberplate = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS, default='Gecss')
    condition = models.CharField(max_length=20, choices=CONDITION, default='New')
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numberplate

    def memNo(self):
        return self.user.username
        
    def client(self):
        return f"{self.user.first_name}  {self.user.last_name}"
