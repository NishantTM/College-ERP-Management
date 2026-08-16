from django.db import models

from students.models import Student
from courses.models import Subject

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),

    ]
    
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student_attendance'
    )
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_attendance')
    
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    
    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date}"