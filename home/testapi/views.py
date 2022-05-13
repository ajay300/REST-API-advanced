#FUNCTION based view

from functools import partial
import json
from pickle import FALSE
from django.shortcuts import render
from .serializers import EmployeeSerializer
from.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.http import JsonResponse
# from django.views.decorators import method_decorator
from testapi import serializers
from django.views import View


# function based view

@csrf_exempt
def employee_detail(request):

    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id' , None)   #if id is blank then will be none
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content='application/json')
        else:
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp , many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content='application/json')
        

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res.values())
            return HttpResponse(json_data , content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type="application/json")

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp , data = "pythondata" , partial=True)
        if  serializer.is_valid():
            serializer.save()
            res = {
                'msg' : 'Success.!'
            }
            JsonResponse(res , safe=True)

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')                                       #third party app request id
        emp = Employee.objects.get(id=id)
        emp.delete() 
        


















'''
def employee_detailID(request , pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data , content_type='application/json')
        '''