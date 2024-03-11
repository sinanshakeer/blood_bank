from django.http import HttpResponseRedirect
from django.shortcuts import render

from login.models import Login

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Login.objects.filter(username=username,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="college":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/college/')
            elif tp=="hospital":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/hospital/')
            elif tp=="student":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/student/')
        else:
            objlist="incorrect username or password......"
            context={
                    'x':objlist,
                }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')