
from django.contrib.auth.models import User
from myapp.models import employee
from rest_framework import serializers

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

'''
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

'''        