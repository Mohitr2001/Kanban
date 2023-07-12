from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users



@api_view(['POST'])
def add_user(request):
    # if request.user.id != 1:
    #     return Response({'error': 'Only the admin can add users.'}, status=403)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(is_admin=False)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
