from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctors)
admin.site.register(Patient)
admin.site.register(Vitals)
admin.site.register(Bills)
admin.site.register(Prescription)
admin.site.register(Diagnosis)
admin.site.register(Appointment)