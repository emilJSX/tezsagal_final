"""tezsagal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Homepage import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from django.urls.conf import include
from Homepage.views import homepage
from DoctorProfile.views import booking
from Appointment.views import schedule_doctor_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="homepage"),
    path("", include("calendarapp.urls")),
    path('', include('Homepage.urls', namespace='doctorprofile')),
    path('', include('Homepage.urls', namespace='doctordataedit')),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view, name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),     
    path('doctorlogin', LoginView.as_view(template_name='login.html')),
    path('patientlogin', LoginView.as_view(template_name='login.html'),name="loginview"),
    path('doctorprofile_edit', views.editprofiledoctor, name="editdoc"),
    path('patientprofile_edit', views.editpatientform, name="editpatient"),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('patient-dashboard', views.patient_dashboard_view, name="patient-dashboard"),
    path('patients-appointments/', views.patient_appointments_doctor, name="patient-appointments"),
    path('addnewepta', views.MemberShipAdd.as_view()),
    path('booking/', booking, name="booking"),
    path('schedule-doctor/', schedule_doctor_view, name="doc_time")


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)







if settings.DEBUG:
    static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
