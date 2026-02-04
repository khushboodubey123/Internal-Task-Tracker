from .serializers import UserCreateSerializer
from rest_framework.decorators import api_view,permission_classes
from resources.common_function import generate_response
from resources.message import (
    SUCCESS_CODE,
    BAD_REQUEST_CODE,
    USER_CREATED_SUCCESSFULLY,
    BAD_REQUEST
)
from rest_framework.permissions import AllowAny

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
