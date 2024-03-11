from django.urls import path, re_path
from student import views

urlpatterns = [
    path('student/', views.student),
    path('manage/', views.manage_student),
    re_path(r'approve/(?P<idd>\w+)', views.approve),
    re_path(r'reject/(?P<idd>\w+)', views.reject),
]