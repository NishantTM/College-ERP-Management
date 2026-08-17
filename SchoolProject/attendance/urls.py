from django.urls import path

from . import views

urlpatterns = [
    path("attendances/", views.attendance_list, name='attendance_list')
]
