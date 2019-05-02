from django.shortcuts import render
from django.contrib.auth.models import User
from .models import employee,teacher,student
from rest_framework import viewsets
from .serializers import employeeSerializer, UserSerializer, studentSerializer, teacherSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class employeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = employee.objects.all().order_by('-eid')
    serializer_class = employeeSerializer  

class studentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = student.objects.all().order_by('-sid')
    serializer_class = studentSerializer  

class teacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = teacher.objects.all().order_by('-tid')
    serializer_class = teacherSerializer  
