from django.urls import path
from rest_framework import serializers
from .views import (PatientListCreateAPIView, PatientDetailView, 
                            VitalsListCreateAPIView, VitalsDetailView,
                            DoctorsListCreateAPIView,
                            DoctorsRetrieveUpdateDestroyAPIView,
                            DiagnosisListCreateAPIView,
                            DiagnosisDetailAPIView,)

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
                                        name='doctors-list'),
    path('doctor_details/<int:pk>/', 
                                DoctorsRetrieveUpdateDestroyAPIView.as_view(),
                                        name='doctor-details'),
    path('patient_diagnosis/<int:patient_pk>/diagnosis/', 
                                        DiagnosisListCreateAPIView.as_view(), 
                                        name='patient-diagnosis'),
    path('patient_diagnosis/<int:pk>/', DiagnosisDetailAPIView.as_view(), 
                                        name='patient-diagnosis-detail')
]