from random import choices
from rest_framework import serializers

GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
class PatientSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    timestamp = serializers.DateTimeField(read_only=True)
    gender = serializers.CharField(choices=GENDER_CHOICES)
    avatar = serializers.ImageField()
    is_active = serializers.BooleanField()
