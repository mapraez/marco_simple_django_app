from django.db import models

# Create your models here.
from datetime import datetime
import random

class School(models.Model):
    name = models.CharField(max_length=400)
    date_of_resumption = models.DateField(default=datetime.today)


    def __str__(self):
        return self.name + f' ({self.id})'

class Faculty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_resumption = models.DateField(default=datetime.today)

    def Get_Name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name + f' ({self.id})'

class Department(models.Model):
    name = models.CharField(max_length=50)
    Faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    date_of_resumption = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name + f' ({self.id})'

class Grade(models.Model):
    name = models.CharField(max_length=50)
    date_of_resumption = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name + f' ({self.id})'

class Certificate_type(models.Model):
    name = models.CharField(max_length=50)
    date_of_resumption = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name + f' ({self.id})'

class Student(models.Model):
    Department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    Grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    School = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    Certificate_type = models.ForeignKey(Certificate_type, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grad_year = models.IntegerField()
    date_of_resumption = models.DateField(default=datetime.today)


    def Get_Name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name + f' ({self.id})'