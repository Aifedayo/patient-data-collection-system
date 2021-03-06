from django.urls import path
from rest_framework import serializers
from .views import (PatientListCreateAPIView, PatientDetailView, 
                    VitalsListCreateAPIView, VitalsDetailView,
                    DoctorsListCreateAPIView, DoctorsRetrieveUpdateDestroyAPIView,
                    DiagnosisListCreateAPIView, BillsListCreateAPIView,
                    BillsDetailAPIView, DiagnosisDetailAPIView, 
                    AppointmentsListCreateAPIView, AppointmentsDetailAPIView, 
                    PrescriptionDetailAPIView, PrescriptionListCreateAPIView,)

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
                                        name='patient-diagnosis-list'),
    path('patient_diagnosis/<int:pk>/', DiagnosisDetailAPIView.as_view(), 
                                        name='patient-diagnosis-detail'),

    path('patient_prescription/<int:patient_pk>/prescription/',
                                        PrescriptionListCreateAPIView.as_view(),
                                        name='patient-prescription-list'),
    path('patient_prescription/<int:pk>/', PrescriptionDetailAPIView.as_view(),
                                        name='patient-prescription-detail'),
    path('patient_bills/<int:patient_id>/bills/', 
                                        BillsListCreateAPIView.as_view(),
                                        name='patient-bills-list'),
    path('patient_bills/<int:pk>/', BillsDetailAPIView.as_view(),
                                        name='patient-bills-detail'),   
    path('patient_appointment/<int:patient_id>/appointments/',
                                        AppointmentsListCreateAPIView.as_view(),
                                        name='patient-appointment-list'),
    path('patient_appointment/<int:pk>/', AppointmentsDetailAPIView.as_view(),
                                        name='patient-appointment-detail'),
]