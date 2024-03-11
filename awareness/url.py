from django.urls import path
from awareness import views

urlpatterns = [
    path('awareness/', views.awareness),
    path('view_stud/', views.view_awareness),
    path('view_user/', views.view_awareness_user),
]