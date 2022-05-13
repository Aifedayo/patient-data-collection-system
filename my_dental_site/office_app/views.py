from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import AddPatient ,AddPatientVitals
from django.views.generic import DetailView, FormView, ListView


class HomeView(ListView):
    model = Patient
    queryset = Patient.objects.all().order_by('-id')
    context_object_name = 'patients'


class AddPatientFormView(FormView):
    template_name = 'office_app/add_patient.html'
    form_class = AddPatient
    success_url = '/office_app/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def patient_vitals(request, patient_id):
    try:
        patient_vitals = Vitals.objects.get(patient_id=patient_id)
        context = {'patient_vitals': patient_vitals}
        return render(request, 'office_app/patient_detail.html', context)
    except ObjectDoesNotExist:
        patient = Patient.objects.get(pk=patient_id)
        context = {'patient': patient}
        return render(request, 'office_app/no_detail.html', context)


class AddPatientVitalsFormView(FormView):
    form_class = AddPatientVitals
    template_name = 'office_app/add_patient_vitals.html'
    success_url = ''

    def form_valid(self, patient_id, form):
        patient = Patient.objects.get(pk=patient_id)
        patient_field = form.save(commit=False)
        patient_field.patient = patient
        patient_field.save()
        return super().form_valid(form)
        

def add_patient_vitals(request, patient_id):
    if request.method == "POST":
        patient = Patient.objects.get(pk=patient_id)
        formset = AddPatientVitals(request.POST)
        if formset.is_valid():
            patient_field = formset.save(commit=False)
            patient_field.patient = patient
            patient_field.save()
            return redirect(reverse('office_app:patient_vitals', kwargs={'patient_id':patient_id}))
    else:
        formset = AddPatientVitals()
    return render(request, 'office_app/add_patient_vitals.html', {'formset': formset})
