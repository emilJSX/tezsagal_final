from email.policy import default
from operator import ge
from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.





departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]



gender=[('Kişi','Kişi'),
('Qadın', 'Qadın')]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/')
    address = models.CharField(max_length=40)
    gender = models.CharField(max_length=1000, choices=gender)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_number(self):
        return self.user.mobile+" "+self.user.mobile

    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

    # def image(self):
    #     if not self.profile_pic:
    #         return '/static/assets/img/doctor01.jpg'
    #     return self.profile_pic.url



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=1000,null=True,blank=True)
    gender = models.CharField(max_length=1000, choices=gender)
    admitDate=models.DateField(auto_now=True,null=True,blank=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    def get_number(self):
        return self.user.mobile

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)




class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


# class CustomerUserPanel(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True)
#     full_name = models.CharField(max_length=10000)
#     short_text = models.CharField(max_length=1000)
#     speciality = models.CharField(max_length=10000)
#     location = models.CharField(max_length=10000)
#     about = models.TextField(max_length=100000)
#     education = models.TextField(max_length=10000)
#     education_start_date = models.DateField()
#     education_end_date = models.DateField()
#     work_experience_name = models.CharField(max_length=1000)
#     work_experience_start_date = models.DateField()
#     work_experience_end_date = models.DateField()
#     service = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.user

