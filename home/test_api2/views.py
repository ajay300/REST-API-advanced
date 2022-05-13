# Class Based View(View)


from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from .models import EmployeeCircle
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapi.models import Employee
import io 
from rest_framework.parsers import JSONParser
from .serializers import EmployeeSerializer
from test_api2 import serializers
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt , name='dispatch')
class EmployeevAPI(View):
    
    def get(self,request , *args , **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id' , None)   #if id is blank then will be none
        if id is not None:
            emp = EmployeeCircle.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content='application/json')
        else:
            emp = EmployeeCircle.objects.all()
            serializer = EmployeeSerializer(emp , many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content='application/json')

    def post(self,request , *args,**kwargs):
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

    def put(self,request , *args , **kwargs):
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

    def delete(self,request,*args , **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')                                       #third party app request id
        emp = Employee.objects.get(id=id)
        emp.delete() 
        res = {
            'msg':'Data Deleted'
        }
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data , content='application/json')
        