from .serializers import UserCreateSerializer,UserSerializer
from rest_framework.decorators import api_view,permission_classes
from resources.common_function import generate_response
from resources.message import (
    SUCCESS_CODE,
    BAD_REQUEST_CODE,
    USER_CREATED_SUCCESSFULLY,
    BAD_REQUEST,INTERNAL_SERVER_ERROR,DATA_RETRIEVED_SUCCESSFULLY 
)
from rest_framework.permissions import AllowAny
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return generate_response(
            BAD_REQUEST_CODE,
            BAD_REQUEST,
            error_message=serializer.errors
        )

    serializer.save()
    return generate_response(
        SUCCESS_CODE,
        USER_CREATED_SUCCESSFULLY,
        serializer.data
    )


@api_view(['GET'])
def user_list(request):
    try:
        users = User.objects.filter(is_active=True)
        serializer = UserSerializer(users, many=True)

        return generate_response(
            SUCCESS_CODE,
            DATA_RETRIEVED_SUCCESSFULLY,
            serializer.data
        )

    except Exception as e:
        return generate_response(
            BAD_REQUEST_CODE,
            INTERNAL_SERVER_ERROR,
            error_message=str(e)
        )
    
 
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer   