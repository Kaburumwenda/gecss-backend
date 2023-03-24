from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class BatteryResource(ImportExportModelAdmin, admin.ModelAdmin ):
    pass

class BatterySwapAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass


class BatteryStationAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass



admin.site.register(Battery, BatteryResource)
admin.site.register(BatteryStation, BatteryStationAdmin)
admin.site.register(BatterySwap, BatterySwapAdmin)