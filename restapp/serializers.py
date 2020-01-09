from rest_framework import serializers
from .models import employees,Student
# from .models import employees
class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        # fields = ('first_name','last_name')
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
