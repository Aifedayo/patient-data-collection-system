from django.urls import path
from .views import *
from . import views

app_name = 'office_app'

urlpatterns = [
    path('', HomeView.as_view(), name='list_patients'),
    path('patient_detail/<int:patient_id>/', views.patient_vitals, name='patient_detail'),
    path('add_patient/', AddPatientFormView.as_view(), name='add_patient'),
    path('add_patient_vitals/<int:patient_id>/', views.add_patient_vitals, name='add_patient_vitals'),
]