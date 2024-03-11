from django.urls import path
from temp import views

urlpatterns = [
    path('home/', views.home),
    path('college/', views.college),
    path('student/', views.student),
    path('user/', views.user),
    path('hospital/', views.hospital),
]