from django.contrib import admin
from .models import School, Student, Faculty, Department, Grade, Certificate_type

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_type)