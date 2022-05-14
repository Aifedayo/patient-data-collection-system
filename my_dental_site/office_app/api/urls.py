from django.urls import path
from rest_framework import serializers
from .views import *

urlpatterns = [
    path('patient_lists/', patient_list_create_api_view, name='patient_lists'),
]