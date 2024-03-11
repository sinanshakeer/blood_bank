from django.urls import path
from hospital import views

urlpatterns = [
    path('hospital/', views.hospital),
    path('view_hos_user/', views.view_hos_user),
]