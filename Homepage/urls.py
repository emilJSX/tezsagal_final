from django.urls import path

from . import views
app_name = 'home'

urlpatterns = [
    path('doctorprofile/<int:pk>/', views.DoctorProfileView.as_view(), name="doctorprofile"),
    path('profile/<int:pk>/', views.editpatientform, name="profile_edit"),
]           