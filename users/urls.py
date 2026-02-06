from django.urls import path
from .views import create_user,user_list
from .views import CustomTokenObtainPairView
urlpatterns = [
    path('create-user', create_user, name='create_user'),
    path('user-list',user_list,name='user_list'),
    path(
        "auth/login",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair"
    )
]
