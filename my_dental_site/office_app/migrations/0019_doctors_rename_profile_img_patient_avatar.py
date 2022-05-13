# Generated by Django 4.0 on 2022-05-13 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0018_alter_bills_options_alter_diagnosis_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid3, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10, null=True)),
                ('years_of_experience', models.IntegerField(default=1)),
                ('rank', models.CharField(choices=[('Department Head', 'Department Head'), ('Team Lead', 'Team Lead'), ('Supervisor', 'Supervisor'), ('Director', 'Director'), ('Chief Medical Director', 'Chief Medical Director')], max_length=30, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/images/models')),
                ('shift', models.CharField(choices=[('On Shift', 'On Shift'), ('Off Shift', 'Off Shift')], max_length=25, null=True)),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Break', 'Break'), ('On Leave', 'On Leave'), ('Closed', 'Closed')], max_length=30, null=True)),
                ('department', models.CharField(choices=[('Consultant', 'Consultant'), ('Intern', 'Intern'), ('Resident Doctor', 'Resident Doctor')], max_length=30, null=True)),
                ('specialization', models.CharField(choices=[('Paediatrics', 'Paediatrics'), ('Ophthalmology', 'Ophthalmology'), ('Oncology', 'Oncology'), ('Podiatry', 'Podiatry'), ('Surgery', 'Surgery'), ('Psychiatry', 'Psychiatry'), ('Neurology', 'Neurology'), ('OB/Gyn', 'OB/Gyn'), ('Orthopaedic', 'Orthopaedic'), ('Radiology', 'Radiology'), ('Pathology', 'Pathology'), ('Urology', 'Urology')], max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='profile_img',
            new_name='avatar',
        ),
    ]
