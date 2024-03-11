from django.http import HttpResponseRedirect
from django.shortcuts import render
from hospital.models import Hospital
import datetime

from login.models import Login
# Create your views here.
def hospital(request):
    if request.method=='POST':
        obj=Hospital()
        obj.register_no=request.POST.get('no')
        obj.name=request.POST.get('name')
        obj.location=request.POST.get('location')
        obj.phone=request.POST.get('phone')
        obj.email=request.POST.get('email')
        obj.started_date=request.POST.get('year')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.save()
        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type='hospital'
        ob.u_id=obj.hospital_id
        ob.save()
        return HttpResponseRedirect('/temp/home/')
    return render(request,'hospital/hospital.html')


def view_hos_user(request):
    obj=Hospital.objects.all()
    context={
        'x':obj
    }
    return render(request,'hospital/view_hos_user.html',context)