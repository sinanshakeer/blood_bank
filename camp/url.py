from django.urls import path, re_path
from camp import views

urlpatterns = [
    path('add_camp/', views.add_camp),
    path('manage_camp/', views.manage_camp),
    path('view_camp_hos/', views.view_camp_hos),
    path('view_camp_stud/', views.view_camp_stud),
    path('view_camp_user/', views.view_camp_user),
    re_path(r'edit/(?P<idd>\w+)', views.edit),
    re_path(r'delete/(?P<idd>\w+)', views.delete),
]