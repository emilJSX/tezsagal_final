from telnetlib import STATUS
from django.shortcuts import render,redirect
from .forms import AppointmentDoctor
from Appointment.models import ScheduleRecord

# Create your views here.

def schedule_doctor_view(request):
    """
        endpoint : {domain}/schedule-records-create
    """
    schedule_records = request.user.doctor.schedule.schedule_records.all()

    if request.method == "POST":
        form = AppointmentDoctor(request.POST)
        if form.is_valid():
            schedule_record = form.save(commit=False)
            schedule_record.schedule = request.user.doctor.schedule
            schedule_record.save()
            print("new",schedule_record)
            return redirect('doc_time')
        else:
            print('not valid')

    else:
        form = AppointmentDoctor()

    
    context = {
        "form":form,
        "schedule_records": schedule_records,
    }

    return render(request,'schedule-timings.html',context=context)

def schedule_records_manage_by_doctor(request):

    """
        endpoint : {domain}/schedule-records-create
    """
    
    schedule_records = request.user.doctor.schedule.schedule_records.all()

    if request.method == "POST":
        form = AppointmentDoctor(request.POST)
        if form.is_valid():
            schedule_record = form.save(commit=False)
            schedule_record.schedule = request.user.doctor.schedule
            schedule_record.save()
            return redirect('')

    else:
        form = AppointmentDoctor()

    
    context = {
        "form":form,
        "schedule_records": schedule_records,
    }

    return render(request,'schedule-timings.html',context=context)

def update_some_record(request,pk,status):
    """http://domain/update-record/<pk>/<status>/"""
    
    record= ScheduleRecord.objects.get(pk=pk)
    record.status = status
    record.save()