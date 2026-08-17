from django.urls import path

from .import views

urlpatterns = [
    path("fees/", views.fees_list, name='fees_list')
]
