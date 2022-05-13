from django.contrib import admin
from django.urls import path , include
from . import views
# from testapi  import views 
urlpatterns = [

    path('employee/',views.EmployeevAPI.as_view())
    
]
