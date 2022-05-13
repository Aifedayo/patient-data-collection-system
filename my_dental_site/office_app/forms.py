from django import forms
from .models import *
from django.forms import ModelForm

class AddPatient(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    error_messages = {
        'age': {
            'min_value': 'Minimum value is 1'
        }
    }

class AddPatientVitals(ModelForm):
    class Meta:
        model = Vitals
        fields = '__all__'
        exclude = ['patient']