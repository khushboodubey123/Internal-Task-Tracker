from django.urls import path
from .views import create_user,user_list

urlpatterns = [
    path('create-user', create_user, name='create_user'),
    path('user-list',user_list,name='user_list')
]
