from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_student = ('name','group',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_teachers = ('name','subject',)
    filter_horizontal = ('students',)
