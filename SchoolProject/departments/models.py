from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name
    
