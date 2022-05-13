import random
import string
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.urls import reverse

# Create your models here.
class Patient(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male')
    ]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=1)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    profile_img = models.ImageField(upload_to ='uploads/% Y/% m/% d/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

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