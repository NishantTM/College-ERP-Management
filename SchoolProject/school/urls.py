from django.urls import path
from .import views

urlpatterns = [
    
    # for students
    path("", views.student, name="student"),
    path("student_list/view", views.student_list, name="student_list"),
    path("add_student/add", views.add_student, name="add_student"),
    path("update/<int:id>/", views.update_student, name="update_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    
    # for teachers
    path("teachers", views.teacher, name="teacher"),
    path("teachers/list/", views.teacher_list, name="teacher_list"),
    path("teachers/add/", views.add_teacher, name="add_teacher"),
    path("teachers/modify/<int:id>/", views.modify_teacher, name="modify_teacher"),
    path("teachers/delete/<int:id>/", views.del_teacher, name="del_teacher"),
    
]