from django.urls import path, re_path
from location import views

urlpatterns = [
    path('post_loc/', views.post_loc),
    re_path(r'map/(?P<idd>\w+)', views.map),
    path('view/', views.view_map),
]