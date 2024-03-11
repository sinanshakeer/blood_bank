from django.http import HttpResponseRedirect
from django.shortcuts import render
from camp.models import Camp
from datetime import datetime
# Create your views here.
def add_camp(request):
    if request.method=='POST':
        obj=Camp()
        obj.name=request.POST.get('name')
        obj.details=request.POST.get('details')
        obj.date=request.POST.get('date')
        obj.save()
        return HttpResponseRedirect('/temp/college/')
    return render(request,'camp/add_camp.html')

def manage_camp(request):
    obj=Camp.objects.all()
    context={
        'x':obj
    }
    return render(request,'camp/manage_camp.html',context)


def edit(request,idd):
    ob=Camp.objects.get(camp_id=idd)
    sn=datetime.now()
    date_time=sn.strftime("%Y-%m-%d")
    context={
        'x':ob,
        'y':date_time
    }
    if request.method=='POST':
        obj=Camp.objects.get(camp_id=idd)
        obj.name=request.POST.get('name')
        obj.details=request.POST.get('details')
        obj.status='pending'
        obj.save()
        return manage_camp(request)
    return render(request,'camp/edit_camp.html',context)

def delete(request,idd):
    obj=Camp.objects.get(camp_id=idd)
    obj.delete()
    return manage_camp(request)

def view_camp_hos(request):
    obj=Camp.objects.all()
    context={
        'x':obj
    }
    return render(request,'camp/view_camp_hos.html',context)

def view_camp_stud(request):
    obj=Camp.objects.all()
    context={
        'x':obj
    }
    return render(request,'camp/view_camp_stud.html',context)

def view_camp_user(request):
    obj=Camp.objects.all()
    context={
        'x':obj
    }
    return render(request,'camp/view_camp_user.html',context)

