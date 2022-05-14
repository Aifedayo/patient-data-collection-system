from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (DeleteView, DetailView, FormView, ListView,
                                  UpdateView)

from .forms import AddPatient, AddPatientVitals
from .models import *


class HomeView(ListView):
    model = Patient
    queryset = Patient.objects.all().order_by('-id')
    context_object_name = 'patients'
    extra_context = {'female_patient_count': Patient.objects.filter(gender__exact='Female').count()}
    extra_context = {'male_patient_count': Patient.objects.filter(gender__exact='Male').count()}


def vitals_list(request):
    vitals = Vitals.objects.all()
    data = {'vitals': list(vitals.values())}
    response = JsonResponse(data)
    return response

def vitals_details(request, pk):
    try:
        vitals = Vitals.objects.get(pk=pk)
        data = {
            'vitals': {
                'patient': vitals.patient.full_name,
                'heartrate': vitals.heartrate,
                'height': vitals.height,
                'weight': vitals.weight,
                'blood pressure': vitals.blood_pressure,
                'pulse': vitals.pulse,
            }
        }
        response = JsonResponse(data, status=200)
    except Vitals.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "vitals not found!"
            }
        },
        status=404)
    return response

class DoctorsListView(ListView):
    model = Doctors
    queryset = Doctors.objects.all().order_by('-id')
    context_object_name = 'doctors'

class AddPatientFormView(FormView):
    template_name = 'office_app/patient_form.html'
    form_class = AddPatient
    success_url = '/office_app/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('office_app:list_patients')


class PatientDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # default template name = model_confirm_delete.html
    model = Patient
    success_url = reverse_lazy('office_app:list_patients')


# class PatientVitalsDetail(DetailView):
#     model = Patient
#     context_object_name: 'patient_vitals'

#     def get_context_data(self, **kwargs):
#             context =  super().get_context_data(**kwargs)
#             try:
#                 context['patient_vitals'] = Vitals.objects.get(patient_id=self.get_object().pk)
#                 print(self.get_object().pk)
#             except ObjectDoesNotExist:
#                 patient = self.get_object()
#                 print(patient)
#                 context = {'patient': patient}
#                 return render(self.request, 'office_app/no_detail.html', context)
#             print(context['patient_vitals'])
#             return context

def patient_vitals(request, patient_id):
    try:
        patient_vitals = Vitals.objects.get(patient_id=patient_id)
        context = {'patient_vitals': patient_vitals}
        return render(request, 'office_app/patient_detail.html', context)
    except ObjectDoesNotExist:
        patient = Patient.objects.get(pk=patient_id)
        context = {'patient': patient}
        return render(request, 'office_app/no_detail.html', context)



def add_patient_vitals(request, patient_id):
    if request.method == "POST":
        patient = Patient.objects.get(pk=patient_id)
        formset = AddPatientVitals(request.POST)
        if formset.is_valid():
            patient_field = formset.save(commit=False)
            patient_field.patient = patient
            patient_field.save()
            return redirect(reverse('office_app:patient_detail', kwargs={'patient_id':patient_id}))
    else:
        formset = AddPatientVitals()
    return render(request, 'office_app/add_patient_vitals_form.html', {'formset': formset})

