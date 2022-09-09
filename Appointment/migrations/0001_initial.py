# Generated by Django 4.0.5 on 2022-08-30 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Homepage', '0009_alter_patient_address_alter_patient_admitdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='Homepage.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Confirmed'), (3, 'Canceled'), (4, 'Edited')], default=1)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('paid', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_records', to='Homepage.patient')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_records', to='Appointment.schedule')),
            ],
        ),
    ]
