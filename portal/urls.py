from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('admin-alerts/', views.admin_notifications, name='admin_notifications'),
]