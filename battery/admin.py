from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Battery)
admin.site.register(BatteryStation)
admin.site.register(BatterySwap)