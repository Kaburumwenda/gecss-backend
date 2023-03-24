from django.db import models

# Create your models here.
class Battery(models.Model):
    code = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class BatteryStation(models.Model):
    title = models.CharField(max_length=150)
    head = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.title
 

class BatterySwap(models.Model):
    bike_no = models.CharField(max_length=150)
    mem_no = models.CharField(max_length=100)
    source = models.CharField(max_length=150, default='Online' )
    battery_code1 = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, default='Issued')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bike_no
