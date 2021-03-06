from django.db import models
from django.conf import settings

# Create your models here.
class BatteryStation(models.Model):
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    image = models.ImageField(upload_to='battery_centers')
    charged_battery = models.PositiveIntegerField(default=0)
    discharged_battery = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    def getImage(self):
        if self.image:
            return settings.BASE_URL + self.image.url
        return ''