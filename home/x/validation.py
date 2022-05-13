from rest_framework import serializers
from testapi.models import Employee




class EmployeeSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(read_only=True)   # another method
    class Meta:
        model = Employee
        fields = ['id' , 'name' , 'location']
        read_only_fields = ['name']