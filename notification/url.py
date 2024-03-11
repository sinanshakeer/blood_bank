from django.urls import path
from notification import views

urlpatterns = [
    path('notification/', views.notification),
    path('view_notification_stud/', views.view_notification_stud),
    path('view_notification_user/', views.view_notification_user),
]