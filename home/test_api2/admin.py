from django.contrib import admin
from .models import EmployeeCircle
# Register your models here.


@admin.register(EmployeeCircle)
class EmployeeCircleAdmin(admin.ModelAdmin):
    list_display = ['id','name']
