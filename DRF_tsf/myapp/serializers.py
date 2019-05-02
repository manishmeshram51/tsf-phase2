
from django.contrib.auth.models import User
from myapp.models import employee, teacher, student
from rest_framework import serializers

class teacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'


class studentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

 