from django.urls import path, re_path
from blood_request import views

urlpatterns = [
    path('blood_request/', views.blood_request),
    path('manage_bloodrequest/', views.manage_bloodrequest),
    path('view_acc_br_hos/', views.view_acc_br_hos),
    path('view_bloodrequest_stud/', views.view_bloodrequest_stud),
    path('view_bloodrequest_user/', views.view_bloodrequest_user),
    re_path(r'^approve/(?P<idd>\w+)$', views.approve),
    re_path(r'^reject/(?P<idd>\w+)$', views.reject),
]