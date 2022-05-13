from django.contrib import admin
from .models import Employee
# Register your models here.



# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    list_display = ['id' , 'name' ]

