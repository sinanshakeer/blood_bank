from django.shortcuts import render

from location.models import Location
from student.models import Student
# Create your views here.

def post_loc(request):
    ss=request.session["u_id"]
    if request.method == 'POST':
        obj = Location()
        obj.student_id=ss
        obj.longitude=request.POST.get('long')
        obj.latitude=request.POST.get('lat')
        obj.save()
    return render(request, 'location/add_location.html')

def map(request,idd):
    obj=Location.objects.get(location_id=idd)
    context={
        'lat': obj.latitude,
        'lon': obj.longitude,

    }
    return render(request,'location/map.html',context)


def view_map(request):
    obj=Location.objects.all()
    context={
        'x':obj
    }
    return render(request,'location/view_location.html',context)
