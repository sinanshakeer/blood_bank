from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback/', views.feedback),
    path('view/', views.view_feedback),
]