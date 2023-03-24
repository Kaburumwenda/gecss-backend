from django.contrib import admin
from .models import *
# Register your models here.
class MpesaAdmin(admin.ModelAdmin):
    list_display = ['transactionType', 'transID', 'billRefNumber', 'transTime', 'orgAccountBalance', 'created']

admin.site.register(MpesaCipher)
admin.site.register(MpesaPayment, MpesaAdmin)
admin.site.register(MpesaPay, MpesaAdmin)
