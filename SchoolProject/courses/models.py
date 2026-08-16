from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    # start_date = models.DateField()
    # end_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in years")
    desciption = models.CharField(max_length=300)


class Subject(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="subjects"
    )
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=20, unique=True)
    semester = models.PositiveIntegerField(unique=True)
    credit_hours = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.course.name}"
