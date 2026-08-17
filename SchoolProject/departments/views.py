from django.shortcuts import render
from . models import Department

# Create your views here.
def department_list(request):
    
    department = Department.objects.all()
    
    return render(request, "departments/department_list", {"department" :department})