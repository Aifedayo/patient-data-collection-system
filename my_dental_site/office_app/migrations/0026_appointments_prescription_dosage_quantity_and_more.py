# Generated by Django 4.0 on 2022-05-15 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0025_alter_doctors_avatar_alter_patient_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('next_appointment', models.IntegerField(blank=True, default=0, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointments', to='office_app.patient')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='dosage_quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='dosage_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='consultation_fee',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bills',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_bills', to='office_app.patient'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='prescription_fee',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bills',
            name='registration_fee',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_diagnosis', to='office_app.patient'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_prescription', to='office_app.patient'),
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
