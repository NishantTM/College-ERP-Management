from django.urls import path
from .import views

urlpatterns = [
    
    path("teachers", views.teacher, name="teacher"),
    path("teachers/list/", views.teacher_list, name="teacher_list"),
    path("teachers/add/", views.add_teacher, name="add_teacher"),
    path("teachers/modify/<int:id>/", views.modify_teacher, name="modify_teacher"),
    path("teachers/delete/<int:id>/", views.del_teacher, name="del_teacher"),
]
