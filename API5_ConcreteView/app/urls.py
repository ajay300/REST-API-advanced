# from django.contrib import admin
from django.urls import path 
from . import views
# from testapi  import views 
urlpatterns = [

    #Combo Concrete View
    path('studentview/',views.StudentListcreate.as_view()),
    path('studentadd/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('studentapiremove/<int:pk>',views.StudentRetrieveDestroy.as_view()),
    

    # modelmixin + genericView
    path('studentlapi/',views.StudentList.as_view()),
    path('studentapipost/',views.Studentcreate.as_view()),
    path('studentapi/<int:pk>',views.StudentRetrieve.as_view()),
    path('studentapi/<int:pk>/',views.StudentUdpate.as_view()),
    path('studentapikill/<int:pk>/',views.StudentDestroy.as_view()),
        
    

]
