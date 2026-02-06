from django.urls import path
from .views import create_task,list_tasks,update_task_status

urlpatterns = [
    path('create-task', create_task, name='create_task'),
    path('list-tasks',list_tasks,name='list_tasks'),
    path('update-task-status',update_task_status,name='update_task_status')
]