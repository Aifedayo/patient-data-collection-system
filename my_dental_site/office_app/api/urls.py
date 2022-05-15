from django.urls import path
from rest_framework import serializers
from .views import PatientListCreateAPIView, PatientDetailView

urlpatterns = [
    path('patient_lists/', PatientListCreateAPIView.as_view(), 
                                                        name='patient-lists'),
    path('patient_detail/<int:pk>/', PatientDetailView.as_view(), 
                                                        name='patient-detail'),
]