
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class GecssBranchAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass


class BatteryStationAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass

admin.site.register(BatteryStation, BatteryStationAdmin)
admin.site.register(GecssBranch, GecssBranchAdmin)
admin.site.register(AgentNotification)
admin.site.register(CompanyTrend)
