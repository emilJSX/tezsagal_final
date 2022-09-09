from django import forms
from django.contrib.auth.models import User
from .models import *

class AppointmentDoctor(forms.ModelForm):
    # date = forms.DateField()
    # start_time = forms.TimeField()
    # end_time = forms.TimeField()
    class Meta:
        model = ScheduleRecord
        fields = ['date', 'start_time', 'end_time']