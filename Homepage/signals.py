from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from Homepage.models import Doctor
from Appointment.models import Schedule

@receiver(post_save,sender=Doctor)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Schedule.objects.create(doctor=instance)

