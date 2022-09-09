from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from . import models
from django.forms import modelformset_factory
# from django.forms import ModelForm
from .models import Doctor, Patient


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }



class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','profile_pic']

MemberShipFormSet = modelformset_factory(
    Doctor, fields=['address'], extra=1
)
MemberShipFormSeting = modelformset_factory(
    Doctor, fields=['mobile'], extra=1
)


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','profile_pic']

class UpdatePatientProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Patient
        fields = ['avatar', 'username', 'address', 'number', 'email', 'gender']