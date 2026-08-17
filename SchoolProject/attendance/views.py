from django.shortcuts import render
from . models import Attendance


# Create your views here.
def attendance_list(request):
    
    attendances = Attendance.objects.all()
    return render(request, "attendance/attendance_list.html", {attendances: "attendances"})