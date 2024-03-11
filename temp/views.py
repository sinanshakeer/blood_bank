from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')

def college(request):
    return render(request,'temp/college.html')

def student(request):
    return render(request,'temp/student.html')

def user(request):
    return render(request,'temp/user.html')

def hospital(request):
    return render(request,'temp/hospital.html')