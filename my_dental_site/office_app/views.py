from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import AddPatient ,AddPatientVitals
from django.views.generic import UpdateView, FormView, ListView, DeleteView


class HomeView(ListView):
    model = Patient
    queryset = Patient.objects.all().order_by('-id')
    context_object_name = 'patients'


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

