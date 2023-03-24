
from django.db import models
from django.conf import settings

# Create your models here.
class BatteryStation(models.Model):
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    charged_battery = models.PositiveIntegerField(default=0)
    discharged_battery = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    def getImage(self):
        if self.image:
            return settings.BASE_URL + self.image.url
        return ''


class GecssBranch(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Dormant', 'Dormant'),
        ('Agent', 'Agent'),
        ('Ongoing', 'Ongoing'),
        ('Construction', 'Construction'),
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Active' )
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AgentNotification(models.Model):
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=555)
    status = models.CharField(max_length=50, default='Active' )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CompanyTrend(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='company/trends', blank=True)
    imgurl = models.CharField(max_length=1024, blank=True)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Active')

    def __str__(self):
        return self.title

    def Imgsrc(self):
        if self.image:
            return settings.BASE_URL + self.image.url
        return ''