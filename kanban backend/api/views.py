from django.shortcuts import render



# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,TaskSerializer
from .models import Users,Status,Priority,Issues,Storypoints
from django.contrib.auth import authenticate
from django.http import JsonResponse



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
        priority_name = request.data.get('priority_name')
        story_value = request.data.get('story_value')

        try:
            status = Status.objects.get(status_name=status_name)
        except Status.DoesNotExist:
            return Response({'error': 'Invalid status name'}, status=400)

        try:
            assignee = Users.objects.get(user_name=assignee_username)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid assignee username'}, status=400)

        try:
            reporter = Users.objects.get(user_name=reporter_username)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid reporter username'}, status=400)
        
        try:
            priority = Priority.objects.get(priority_name=priority_name)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid Priority name'}, status=400)
        
        try:
            storypoints = Storypoints.objects.get(story_value=story_value)
        except Storypoints.DoesNotExist:
            return Response({'error': 'Invalid Story Point'}, status=400)

        serialized.validated_data['status_id_fk'] = status
        serialized.validated_data['assignee_id'] = assignee.user_id
        serialized.validated_data['reporter_id'] = reporter.user_id
        serialized.validated_data['priority_id_fk'] = priority
        serialized.validated_data['story_point_id_fk'] = storypoints
        

        serialized.save()
        return Response(serialized.data, status=201)
    return Response(serialized.errors, status=400)



@api_view(['DELETE'])
def delete_issue(request, issue_id):
    try:
        issue = Issues.objects.get(pk=issue_id)
        issue.delete()
        return Response({'message': 'Issue deleted successfully'}, status=200)
    except Issues.DoesNotExist:
        return Response({'error': 'Invalid issue ID'}, status=404)
    
    


# @api_view(['PUT'])
# def update_task(request, issue_id):
#     try:
#         task = Issues.objects.get(pk=issue_id)
#     except Issues.DoesNotExist:
#         return Response({'error': 'Invalid issue ID'}, status=404)

#     serialized = TaskSerializer(instance=task, data=request.data, partial=True)
#     if serialized.is_valid():
#         serialized.save()
#         return Response(serialized.data, status=200)
#     return Response(serialized.errors, status=400)


# @api_view(['PUT'])
# def update_task(request, issue_id):
#     try:
#         task = Issues.objects.get(pk=issue_id)
#     except Issues.DoesNotExist:
#         return Response({'error': 'Invalid issue ID'}, status=404)

#     serialized = TaskSerializer(instance=task, data=request.data, partial=True)
#     if serialized.is_valid():
#         assignee_id = request.data.get('assignee_id')
#         reporter_id = request.data.get('reporter_id')
#         project_id = request.data.get('project_id_fk')
#         status_id = request.data.get('status_id_fk')

#         try:
#             assignee = Users.objects.get(pk=assignee_id)
#         except Users.DoesNotExist:
#             return Response({'error': 'Invalid assignee ID'}, status=400)

#         try:
#             reporter = Users.objects.get(pk=reporter_id)
#         except Users.DoesNotExist:
#             return Response({'error': 'Invalid reporter ID'}, status=400)

#         try:
#             project = Project.objects.get(pk=project_id)
#         except Project.DoesNotExist:
#             return Response({'error': 'Invalid project ID'}, status=400)

#         try:
#             status = Status.objects.get(pk=status_id)
#         except Status.DoesNotExist:
#             return Response({'error': 'Invalid status ID'}, status=400)

#         serialized.validated_data['assignee_id'] = assignee
#         serialized.validated_data['reporter_id'] = reporter
#         serialized.validated_data['project_id_fk'] = project
#         serialized.validated_data['status_id_fk'] = status

#         serialized.save()
#         return Response(serialized.data, status=200)
#     return Response(serialized.errors, status=400)

# @api_view(['POST'])
# def login(request):
    
#     email = request.data.get('email')
#     password = request.data.get('password')

#     # Authenticate user
#     user = authenticate(email=email, password=password)

#     if user is not None:
#         # User credentials are valid
#         return Response({'message': 'User logged in successfully'}, status=200)
#     else:
#         # Invalid credentials
#         return Response({'error': 'Invalid credentials'}, status=401)


def get_all_statuses(request):
    statuses = Status.objects.all()
    status_list = []

    for status in statuses:
        status_data = {
            'status_id': status.status_id,
            'status_name': status.status_name,
        }
        status_list.append(status_data)

    return JsonResponse({'statuses': status_list})

@api_view(['GET'])
def get_priorities(request):
    priorities = Priority.objects.all()
    priority_list = []

    for priority in priorities:
        priority_data = {
            'priority_id': priority.priority_id,
            'priority_name': priority.priority_name,
        }
        priority_list.append(priority_data)

    return JsonResponse({'priorities': priority_list})
    


@api_view(['GET'])
def get_story_points(request):
    story_points = Storypoints.objects.all()
    story_point_list = []

    for story_point in story_points:
        story_point_data = {
            'story_id': story_point.story_id,
            'story_value': story_point.story_value,
        }
        story_point_list.append(story_point_data)

    return JsonResponse({'story_points': story_point_list})