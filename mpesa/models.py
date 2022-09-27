from django.db import models
from django.contrib.auth.models import User

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