from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.add_user, name='add_user'),
    path('createTask/', views.create_task, name='createTask'),
   
]