from django.shortcuts import render
from . models import Courses, Subject

# Create your views here.

def course_list(request):
    
    courses = Courses.objects.all()
    
    # subject = Subject.objects.all()
    return render(request, "courses/course_list.html", {"courses":courses})