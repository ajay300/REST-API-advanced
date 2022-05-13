# Function based (API VIEW) 

from functools import partial
from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET','POST' , 'PUT','DELETE'])
def StudentApi_view(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            stu = Students.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else: # means id have some data
            stu = Students.objects.all()
            serializer = StudentSerializer(stu , many = True)
            return Response(serializer.data)

    if request.method == "POST":
        # data = request.data
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Added successfully.!'}
            return Response(res)
        return Response(serializer.errors)

    if request.method == "PUT":
        id = request.data.get('id')
        stu = Students.objects.get(id=id)
        serializer = StudentSerializer(stu , data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated Successfully.'}
            return Response(res.values())
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id = request.data.get('id')
        stu = Students.objects.get(id=id)
        stu.delete()
        return Response({'mgs':'DELETE'})