from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)
admin.site.register(Vitals)