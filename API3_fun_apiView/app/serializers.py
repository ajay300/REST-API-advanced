from rest_framework import serializers
from .models import Students



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['seat_no','name','phone','std']

        def validate_seat_no(self , value):
        
            if value >= 20 or value == 15:
                raise serializers.ValidationError('selt full')
            return value