from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework import serializers
from office_app.models import Patient, Doctors

class PatientSerializer(serializers.ModelSerializer):

    time_since_admitted = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        exclude = ('assigned_doctor',)

    def get_time_since_admitted(self, object):
        timestamp = object.timestamp
        print(timestamp)
        now = datetime.now(timezone.utc)
        time_delta = timesince(timestamp, now)
        return time_delta

    # Define an Object layer validation
    def validate(self, data):
        if data['age'] < 0:
            raise serializers.ValidationError('Age cannot be a negative value!!!')
        return data

    # Define a field level validation
    def validate_phone_number(self, value):
        if len(value) < 11:
            raise serializers.ValidationError('Phone number cannot be lesser then 11 digits!!!')
        return value
    