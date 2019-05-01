from django.shortcuts import render
from django.contrib.auth.models import User
from .models import employee
from rest_framework import viewsets
from .serializers import employeeSerializer,UserSerializer

'''
class emplyeeList (APIView):
	def get(self,request):
		employee = employee.objects.all()
		serializer = employeeSerializer(employee1, many=true)
	return Response(serializer.data)

	def post (self):
		pass

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

'''

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
