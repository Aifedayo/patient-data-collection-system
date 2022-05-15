from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from office_app.models import Patient, Doctors

class PatientSerializer(serializers.ModelSerializer):

    #time_since_admitted = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        exclude = ['assigned_doctor']

    # def get_time_since_admitted(self, object):
    #     timestamp = object.timestamp
    #     now = datetime.now()
    #     time_delta = timesince(timestamp, now)
    #     return time_delta
