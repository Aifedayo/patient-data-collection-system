# Generated by Django 4.0 on 2022-05-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_app', '0009_alter_vitals_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vitals',
            old_name='BP',
            new_name='blood_pressure',
        ),
        migrations.AlterField(
            model_name='vitals',
            name='height',
            field=models.DecimalField(decimal_places=1, default=2.5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='vitals',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=2.5, max_digits=5),
        ),
    ]
