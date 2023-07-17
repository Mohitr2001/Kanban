from django.urls import path
from . import views
urlpatterns = [
    path('users/', views.add_user, name='add_user'),
    path('createTask/', views.create_task, name='create_Task'),
    path('issues/<int:issue_id>/delete/', views.delete_issue, name='delete_issue'),
    # path('login/', views.login, name='login'),
    path('getStatus/', views.get_all_statuses, name='getstatus'),
    path('get_priorities/', views.get_priorities, name='getPriorityOptions'),
    path('get_story_points/', views.get_story_points, name='getStoryPoints'),
    
    
     
   
]




# path('issues/<int:issue_id>/update/', views.update_task, name='update_task'),