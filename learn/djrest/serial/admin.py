from django.contrib import admin
from . import models


@admin.register(models.student_data)
class admin_site_data(admin.ModelAdmin):
    list_display = ['id' ,'students_name', 'student_subject', 'student_age']

# Register your models here.
