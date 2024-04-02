from django.db import models


class student_data(models.Model):
    students_name = models.CharField(max_length=50)
    student_subject = models.CharField(max_length=100)
    student_age = models.IntegerField()

# Create your models here.
#I create complex data 
# next I will convert it to python native data 
# next python native data to json()