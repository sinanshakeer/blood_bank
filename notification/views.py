from django.http import HttpResponseRedirect
from django.shortcuts import render
from notification.models import Notifiaction
import datetime
# Create your views here.
def notification(request):
    if request.method=='POST':
        obj=Notifiaction()
        obj.notification=request.POST.get('notification')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
        return HttpResponseRedirect('/temp/college/')
    return render(request,'notification/notification.html')


def view_notification_stud(request):
    obj=Notifiaction.objects.all()
    context={
        'x':obj
    }
    return render(request,'notification/view_notification_stud.html',context)

def view_notification_user(request):
    obj=Notifiaction.objects.all()
    context={
        'x':obj
    }
    return render(request,'notification/view_notification_user.html',context)