from django.urls import path

from . import views

urlpatterns = [
    path("result/", views.result_list, name="result_list"),
]
