from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=6)
    name =models.CharField(max_length=40)
    branch = models.CharField(max_length=50)
    student_class = models.CharField(max_length=20)
    section = models.CharField(max_length=1)


    def __str__(self):
        return self.name