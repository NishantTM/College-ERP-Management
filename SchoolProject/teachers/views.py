from django.shortcuts import render, redirect
from.models import Teacher

# Create your views here.

def teacher(request):
    
    teachers = Teacher.objects.all()
    return render (request, "teachers/teacher.html", {"teachers": teachers})


def teacher_list(request):
    teachers = Teacher.objects.all()
    
    return render(request, "teachers/teacher.html", {"teachers":teachers})


def add_teacher(request):
    

    if request.method == "POST":
        
        Teacher.objects.create(
            
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        phone = request.POST.get("phone"),
        subject = request.POST.get("subject"),
        address = request.POST.get("address") 
      
        )
        
        return redirect("teacher")
    
    return render(request, "teachers/add_teacher.html")

def modify_teacher(request, id):
    
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == "POST":
        teacher.name = request.POST.get("name")
        teacher.email = request.POST.get("email")
        teacher.phone = request.POST.get("phone")
        teacher.subject = request.POST.get("subject")
        teacher.address = request.POST.get("address") 
            
        teacher.save()
        return redirect("teacher")
    
    return render(request, "teachers/modify_teacher.html", {
    "teacher": teacher
})

def del_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect("teacher")
    
    
    return render(request, "teachers/del_teacher.html", {"teacher":teacher} )
