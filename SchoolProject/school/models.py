from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField()
    roll_no = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField(max_length=15)
    subject = models.CharField()
    address = models.TextField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
# class Attendance(models.Model):
#     stu_name = models.CharField(max_length=30)
#     stu_roll = models.IntegerField(max_length=10)



class Title(models.Model):
    title = models.CharField(max_length= 100)
    
    
    def __str__(self):
        return self.title