from asyncore import read
from datetime import datetime, timezone
from tkinter.tix import Tree
from django.utils.timesince import timesince
from rest_framework import serializers
from office_app.models import (Patient, Doctors, 
                                Vitals, Diagnosis, 
                                Prescription, Bills, Appointments)

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Prescription
        fields = '__all__'


class BillsSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Bills
        fields = '__all__'


class AppointmentsSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Appointments
        fields = '__all__'


class DoctorsSerializer(serializers.ModelSerializer):
    
    full_name = serializers.ReadOnlyField()
    is_available = serializers.ReadOnlyField()
    doctor_diagnosis = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Doctors
        fields = '__all__'



class DiagnosisSerializer(serializers.ModelSerializer):
    
    patient = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Diagnosis
        fields = '__all__'
        

class VitalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vitals
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    patient_vitals = VitalsSerializer(many=True, read_only=True)
    patient_diagnosis = DiagnosisSerializer(many=True, read_only=True)
    assigned_doctor = serializers.StringRelatedField(many=True)
    patient_prescription = PrescriptionSerializer(many=True, read_only=True)

    # Method Fields
    time_since_admitted = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_time_since_admitted(self, object):
        timestamp = object.timestamp
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
