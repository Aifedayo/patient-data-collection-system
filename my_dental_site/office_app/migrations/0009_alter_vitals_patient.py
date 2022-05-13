# Generated by Django 4.0 on 2022-05-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0008_patient_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitals',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_vitals', to='office_app.patient'),
        ),
    ]