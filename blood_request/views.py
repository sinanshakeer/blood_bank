from django.http import HttpResponseRedirect
from django.shortcuts import render
from blood_request.models import BloodRequest
import datetime
# Create your views here.
def blood_request(request):
    if request.method=='POST':
        obj=BloodRequest()
        obj.bloodgroup=request.POST.get('bloodGroup')
        obj.unit=request.POST.get('unit')
        obj.hospital_id=1
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/temp/hospital/')
    return render(request,'blood_request/blood_request.html')

def manage_bloodrequest(request):
    obj=BloodRequest.objects.all()
    context={
        'x':obj
    }
    return render(request,'blood_request/manage_bloodrequest.html',context)

def approve(request,idd):
    obj=BloodRequest.objects.get(blood_id=idd)
    obj.status='approve'
    obj.save()
    return  manage_bloodrequest(request)
def reject(request,idd):
    obj=BloodRequest.objects.get(blood_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_bloodrequest(request)

def view_acc_br_hos(request):
    obj=BloodRequest.objects.filter(status='approve')
    context={
        'x':obj
    }
    return render(request,'blood_request/view_acc_br_hos.html',context)

def view_bloodrequest_stud(request):
    obj=BloodRequest.objects.filter(status='approve')
    context={
        'x':obj
    }
    return render(request,'blood_request/view_bloodrequest_stud.html',context)

def view_bloodrequest_user(request):
    obj=BloodRequest.objects.filter(status='approve')
    context={
        'x':obj
    }
    return render(request,'blood_request/view_bloodrequest_user.html',context)