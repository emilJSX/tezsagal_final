import sched
from django.db import models
from Homepage.models import Doctor, Patient
# Create your models here.


class Schedule(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name="schedule")

    def __str__(self) -> str:
        return f"{self.doctor.user}"

class ScheduleRecord(models.Model):
    STATUS_CHOICES = (
        (1, 'Created'),
        (2, 'Pending'),
        (3, 'Confirmed'),
        (4, 'Canceled'),
        (5, 'Edited'),
    )

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="schedule_records",blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="schedule_records", blank=True, null=True)
    # service_name = models.CharField(max_length=10000)
    # description = models.TextField(max_length=100000)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, blank=True)

    created = models.DateTimeField('created at', auto_now_add=True)
    updated = models.DateTimeField('updated at', auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.schedule.doctor} {self.start_time}-{self.end_time}" 