from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees,Student
from .serializers import employeesSerializer,StudentSerializer


class employeesList(APIView):


    def get(self,request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1,many=True)
        return Response(serializer.data)

    def post(self,request):

            return Response(employees.objects.all())

class StudentList(APIView):
    def get(self,request):
        student1 = Student.objects.all()
        serializer = StudentSerializer(student1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
