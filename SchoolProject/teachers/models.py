from django.db import models

# Create your models here.
class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField()
    address = models.TextField(max_length=50)
    
    
    qualification = models.CharField(max_length=200, blank=True)
    
    joining_date = models.DateField(null=True, blank=True)
    
    designation = models.CharField(max_length=100, default='Lecturer')
    
    def __str__(self):
        return self.name