import datetime
from datetime import timedelta

from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinLengthValidator, MinValueValidator)
from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

class Doctors(models.Model):
    AVAILABILITY_CHOICES = (
        ('Available', 'Available'),
        ('Break', 'Break'),
        ('On Leave', 'On Leave'),
        ('Closed', 'Closed'),
    )

    SHIFT_CHOICES = (
        ('On Shift', 'On Shift'),
        ('Off Shift', 'Off Shift'),
    )

    RANK = (
        ('Department Head', 'Department Head'),
        ('Team Lead', 'Team Lead'),
        ('Supervisor', 'Supervisor'),
        ('Director', 'Director'),
        ('Chief Medical Director', 'Chief Medical Director'),
    )

    DEPARTMENT_CHOICES = (
        ('Consultant', 'Consultant'),
        ('Intern', 'Intern'),
        ('Resident Doctor', 'Resident Doctor')
    )

    SPECIALIZATION_CHOICES = (
        ('Paediatrics', 'Paediatrics'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Oncology','Oncology'),
        ('Podiatry', 'Podiatry'),
        ('Surgery', 'Surgery'),
        ('Psychiatry', 'Psychiatry'),
        ('Neurology', 'Neurology'),
        ('OB/Gyn', 'OB/Gyn'),
        ('Orthopaedic', 'Orthopaedic'),
        ('Radiology', 'Radiology'),
        ('Pathology', 'Pathology'),
        ('Urology', 'Urology'),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    years_of_experience = models.IntegerField(default=1)
    rank = models.CharField(max_length=30, null=True, choices=RANK)
    avatar = models.ImageField(null=True, blank=True)
    shift = models.CharField(max_length=25, choices=SHIFT_CHOICES, null=True)
    availability = models.CharField(max_length=30, choices=AVAILABILITY_CHOICES, null=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, null=True)
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES, null=True)

    class Meta:
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'
    
    def full_name(self):
        return f'Dr. {self.first_name} {self.last_name}'

    def is_available(self):
        return self.shift == 'On Shift' and self.availability == 'Available'


class Patient(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveBigIntegerField()
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    avatar = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    assigned_doctor = models.ManyToManyField(Doctors, blank=True)
    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_male(self):
        if self.gender == 'Male':
            return True

    @property
    def is_female(self):
        if self.gender == 'Female':
            return True

    @property
    def last_updated(self):
        return self.timestamp.date()

    def get_absolute_url(self):
        return reverse('list_patient', kwargs={'pk':self.pk})

    @property
    def patient_card_number(self):
        random_number = self.first_name[0] + self.last_name[0] + '000' + str(self.pk)
        return random_number

    

class Vitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, related_name='patient_vitals')
    heartrate = models.IntegerField(default=60)
    height = models.DecimalField(default=2.5, max_digits=5, decimal_places=1)
    weight = models.DecimalField(default=2.5, max_digits=5, decimal_places=1)
    blood_pressure = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(200)])
    pulse = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(200)])

    def __str__(self):
        return f'{self.patient.full_name}'
    class Meta:
        verbose_name_plural = "Vitals"


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,
                                    related_name='patient_diagnosis')
    diagnosis = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Diagnosis of {self.patient.full_name}"

    class Meta:
        verbose_name_plural = "Diagnosis"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,
                                        related_name='patient_prescription')
    drug = models.CharField(max_length=100, null=True, blank=True)
    dosage_quantity = models.CharField(max_length=100, null=True, blank=True)
    dosage_time = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Prescription for {self.patient.full_name}"    


class Bills(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,
                                                related_name='patient_bills')
    registration_fee = models.FloatField(default=0.0)
    consultation_fee = models.FloatField(default=0.0)
    prescription_fee = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Bills"

    def __str__(self):
        return f"Bill for {self.patient.full_name}"

    def grand_total(self):
        bill_list = [self.registration_fee, self.consultation_fee, 
                        self.prescription_fee
                    ]
        return sum(bill_list)


class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,
                                        related_name='patient_appointments')
    appointment_date = models.DateField(null=True, blank=True)
    next_appointment = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"Appointment details for {self.patient.full_name}"

    def next_appointment_date(self):
        return self.appointment_date + datetime.timedelta(days=self.next_appointment)
