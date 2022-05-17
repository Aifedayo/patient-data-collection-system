# Generated by Django 4.0 on 2022-05-17 20:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0026_appointments_prescription_dosage_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office_app.doctors'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office_app.doctors'),
        ),
    ]
