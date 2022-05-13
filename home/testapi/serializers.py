# from wsgiref.validate import validator
# from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Employee

# field validation 
def starts_with_a(value):

    if value[0].lower() != "a":
        raise serializers.ValidationError('Stats with always A')
    return value


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[starts_with_a])
    phone = serializers.IntegerField()
    email = serializers.EmailField()
    location = serializers.CharField()
    emp_id = serializers.IntegerField()
        

    def create(self , validated_data):
        return Employee.objects.create(**validated_data)

    def update(self , instance , validated_data):       #if validated_data is not valid ... instance.data isalready available
        print(instance.name)
        instance.name = validated_data.get('name' , instance.name)
        print(instance.name)
        instance.phone = validated_data.get('phone' , instance.phone)
        instance.email = validated_data.get('email' , instance.email)
        instance.location = validated_data.get('location' , instance.location)

        instance.save()
        return instance

# ********field level validation*********** 
    '''for One field validation'''
    
    def validate_emp_id(self , value):
        
        if value >= 20 or value == 15:
            raise serializers.ValidationError('selt full')
        return value

# ***** Object level Validation *********
    ''' If we want to validate two aur more field... we should use object level validate'''

    def validate(self , data):
        
        nm = data.get('name')  # name field
        ct = data.get('location')
        e = data.get('email')
        
        if nm.lower() == "karan" and ct.lower() != "gujrat":
            raise serializers.ValidationError("City must be a GUJRAT")
        return data
        
        

        

    


    

