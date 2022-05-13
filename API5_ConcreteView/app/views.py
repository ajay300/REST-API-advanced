from .models import Students
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView , ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView

from app import serializers

# Concrete View : ListAPIView + UpdateAPIView = ListCreateview 

class StudentListcreate(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer



# GenericAPIView + ListModelMixin = ListAPIView

class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class Studentcreate(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentUdpate(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

