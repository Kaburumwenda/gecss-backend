from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass

class ExpenseAdmin(ImportExportModelAdmin, admin.ModelAdmin ):
    pass

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(userAccount)
admin.site.register(Expense, ExpenseAdmin)