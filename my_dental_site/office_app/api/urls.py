from django.urls import path
from rest_framework import serializers
from .views import (PatientListCreateAPIView, PatientDetailView, 
                            VitalsListCreateAPIView, VitalsDetailView,
                            DoctorsListCreateAPIView)

urlpatterns = [
    path('patient_lists/', PatientListCreateAPIView.as_view(), 
                                                        name='patient-lists'),
    path('patient_detail/<int:pk>/', PatientDetailView.as_view(), 
                                                        name='patient-detail'),
    path('patient_vitals/', VitalsListCreateAPIView.as_view(),
                                                        name='patient-vitals'), 
    path('patient_vitals/<int:pk>/', VitalsDetailView.as_view(),
                                                name='patient-vitals-detail'),
    path('doctors_lists/', DoctorsListCreateAPIView.as_view(),
                                                name='doctors-lists'),
]