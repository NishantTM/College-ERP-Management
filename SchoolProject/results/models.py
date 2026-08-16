from django.db import models

from students.models import Student
from courses.models import Subject


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_results")

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_results")

    marks = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.CharField(max_length=15, blank=True)


def __str__(self):
    return f"{self.student.name} - {self.subject.name}"
