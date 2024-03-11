"""blood_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from temp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('awareness/', include('awareness.url')),
    path('blood_request/', include('blood_request.url')),
    path('camp/', include('camp.url')),
    path('camp_request/', include('camp_request.url')),
    path('feedback/', include('feedback.url')),
    path('hospital/', include('hospital.url')),
    path('location/', include('location.url')),
    path('notification/', include('notification.url')),
    path('student/', include('student.url')),
    path('login/', include('login.url')),
    path('temp/', include('temp.url')),
    path('', views.home),
]