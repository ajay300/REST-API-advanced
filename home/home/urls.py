from django.contrib import admin
from django.urls import path , include
# import test_api2
from testapi import views 
# from test_api2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('employee/api/' , views.EmployeeView.as_view())
    path('employee/api/',views.employee_detail),
    path('api/',include('test_api2.urls')),
    path('app3/',include('test_api3.urls')),
    # path('app4/',include('test_api4.urls')),
    path('app5/',include('test_api5.urls'))
    
    
]
