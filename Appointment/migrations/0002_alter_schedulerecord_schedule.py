# Generated by Django 4.0.5 on 2022-08-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerecord',
            name='schedule',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_records', to='Appointment.schedule'),
        ),
    ]
