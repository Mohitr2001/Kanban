from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,TaskSerializer
from .models import Users,Status



@api_view(['POST'])
def add_user(request):
    # if request.user.id != 1:
    #     return Response({'error': 'Only the admin can add users.'}, status=403)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(is_admin=False)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_task(request):
    serialized = TaskSerializer(data=request.data)
    if serialized.is_valid():
        status_name = request.data.get('status_name')
        assignee_username = request.data.get('assignee_username')
        reporter_username = request.data.get('reporter_username')

        try:
            status = Status.objects.get(status_name=status_name)
        except Status.DoesNotExist:
            return Response({'error': 'Invalid status name'}, status=400)

        try:
            assignee = Users.objects.get(username=assignee_username)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid assignee username'}, status=400)

        try:
            reporter = Users.objects.get(username=reporter_username)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid reporter username'}, status=400)

        serialized.validated_data['status_id_fk'] = status.status_id
        serialized.validated_data['assignee_id'] = assignee.user_id
        serialized.validated_data['reporter_id'] = reporter.user_id

        serialized.save()
        return Response(serialized.data, status=201)
    return Response(serialized.errors, status=400)