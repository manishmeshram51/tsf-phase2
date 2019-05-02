from django.contrib import admin
from .models import employee, student, teacher

# Register your models here.
admin.site.register(employee)  
admin.site.register(student) 
admin.site.register(teacher) 