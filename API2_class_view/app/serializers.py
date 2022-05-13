from rest_framework import serializers
from .models import EmployeeCircle





class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCircle
        fields = ['id','name','phone','location'] # or "__all__"

        def validate_name(self , value):
        
            if value == 'ajay':
                raise serializers.ValidationError('selt full')
            return value