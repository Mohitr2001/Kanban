from rest_framework import serializers
from .models import Users, Issues

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_name','email','password']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields ='__all__'