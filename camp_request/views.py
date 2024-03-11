from django.http import HttpResponseRedirect
from django.shortcuts import render
from camp_request.models import CampRequest
import datetime
# Create your views here.
def camprequest(request,idd):
    if request.method=='POST':
        obj=CampRequest()
        obj.request=request.POST.get('request')
        obj.camp_id=idd
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/temp/hospital/')
    return render(request,'camp_request/camprequest.html')

def manage_camp_request(request):
    obj=CampRequest.objects.all()
    context={
        'x':obj
    }
    return render(request,'camp_request/manage_camp_request.html',context)

def approve(request,idd):
    obj=CampRequest.objects.get(request_id=idd)
    obj.status='approve'
    obj.save()
    return  manage_camp_request(request)
def reject(request,idd):
    obj=CampRequest.objects.get(request_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_camp_request(request)

def view_acc_req(request):
    obj=CampRequest.objects.filter(status='approve')
    context={
        'x':obj
    }
    return render(request,'camp_request/view_acc_req.html',context)