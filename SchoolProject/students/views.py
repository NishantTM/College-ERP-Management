from django.shortcuts import render, redirect, get_object_or_404
from.models import Student, Title
# from students.models import Title



# Create your views here.
def student(request):
   
    
    students = Student.objects.all()
    stu = Title.objects.all()
    return render (request, "students/student.html",  {
            "students": students,
            "stu": stu,
        })

def student_list(request):
    students = Student.objects.all()
    
    return render(request, "students/student.html", {"students":students})


def add_student(request):
    

    if request.method == "POST":
        
        Student.objects.create(
            
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        roll_no = request.POST.get("roll_no"),
        phone = request.POST.get("phone"),
        address = request.POST.get("address") 
        )
        
        return redirect("student")
    
    return render(request, "students/add_student.html")

def update_student(request, id):
    
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_no = request.POST.get("roll_no")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.address = request.POST.get("address") 
            
        student.save()
        return redirect("student")
    
    return render(request, "students/update_student.html", {
    "student": student
})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        student.delete()
        return redirect("student")
    
    
    return render(request, "students/delete_student.html", {"student":student} )