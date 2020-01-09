from django.db import models

# Create your models here.
class employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default=True)
    emp_id = models.IntegerField()


    def __str__(self):
        return self.first_name


# create a class for student records
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=40,default=True)
    rollno = models.IntegerField()
    marks = models.DecimalField(max_digits=5,decimal_places=2)


    def __str__(self):
        return self.firstname
