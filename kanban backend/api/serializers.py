from rest_framework import serializers
from .models import Users, Issues,Priority,Status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields='__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields ='__all__'

# class TaskSerializer(serializers.ModelSerializer):
#     assignee = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
#     reporter = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
#     priority_id_fk = serializers.PrimaryKeyRelatedField(queryset=Priority.objects.all())
#     status_id_fk = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())

#     class Meta:
#         model = Issues
#         fields = '__all__'