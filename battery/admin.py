from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class BatteryResource(ImportExportModelAdmin, admin.ModelAdmin ):
    pass

class BatterySwapAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    search_fields = ['bike_no']
    list_filter = ['status']
    list_display = ['bike_no', 'battery_code1', 'mem_no', 'amount', 'status', 'createdAt']


class BatteryStationAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass



admin.site.register(Battery, BatteryResource)
admin.site.register(BatteryStation, BatteryStationAdmin)
admin.site.register(BatterySwap, BatterySwapAdmin)