from django.http import HttpResponseRedirect
from django.shortcuts import render
from awareness.models import Awareness
import datetime
# Create your views here.
def awareness(request):
    if request.method=='POST':
        obj=Awareness()
        obj.awareness=request.POST.get('name')
        obj.details=request.POST.get('details')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
        return HttpResponseRedirect('/temp/college/')
    return render(request,'awareness/awareness.html')

def view_awareness_user(request):
    obj=Awareness.objects.all()
    context={
        'x':obj
    }
    return render(request,'awareness/view_awareness_user.html',context)

def view_awareness(request):
    obj=Awareness.objects.all()
    context={
        'x':obj
    }
    return render(request,'awareness/view_awareness.html',context)