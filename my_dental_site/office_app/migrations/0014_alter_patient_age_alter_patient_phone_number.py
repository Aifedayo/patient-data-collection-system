# Generated by Django 4.0 on 2022-05-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0013_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(default=1),
        ),
    ]
