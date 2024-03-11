from django.http import HttpResponseRedirect
from django.shortcuts import render
from student.models import Student
import datetime

from login.models import Login
# Create your views here.
def student(request):
    if request.method=='POST':
        obj=Student()
        obj.admission_no=request.POST.get('adm')
        obj.name=request.POST.get('name')
        obj.course=request.POST.get('course')
        obj.year=request.POST.get('year')
        obj.phone=request.POST.get('phone')
        obj.dob=request.POST.get('dob')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.bloodgroup=request.POST.get('bloodGroup')
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/temp/home/')
    return render(request,'student/student.html')


def manage_student(request):
    obj=Student.objects.all()
    context={
        'x':obj
    }
    return render(request,'student/manage_student.html',context)

def approve(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='approve'
    obj.save()
    ob=Login()
    ob.username=obj.username
    ob.password=obj.password
    ob.type='student'
    ob.u_id=obj.student_id
    ob.save()
    return  manage_student(request)
def reject(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_student(request)


