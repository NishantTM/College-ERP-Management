# from datetime import timezone

from django.utils import timezone
from django.db import models


# Create your models here.
class Student(models.Model):

    # GENDER_CHOICES = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    #      ('Other', 'Other'),

    # ]
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.TextField(max_length=15)

    # gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    gender = models.CharField(max_length=20, blank=True, null=True)

    date_of_birth = models.DateField(null=True, blank=True)

    admission_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
