# Generated by Django 4.0 on 2022-05-13 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0018_alter_bills_options_alter_diagnosis_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='profile_img',
            new_name='avatar',
        ),
    ]
