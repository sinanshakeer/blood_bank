from django.urls import path, re_path
from camp_request import views

urlpatterns = [
    re_path(r'camprequest/(?P<idd>\w+)', views.camprequest),
    path('manage_camp_request/', views.manage_camp_request),
    path('view_acc_req/', views.view_acc_req),
    re_path(r'approve/(?P<idd>\w+)', views.approve),
    re_path(r'reject/(?P<idd>\w+)', views.reject),
]