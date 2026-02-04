import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskCreateSerializer
from resources.common_function import generate_response
from resources.message import TASK_CREATED_SUCCESSFULLY, BAD_REQUEST,CREATED_CODE,BAD_REQUEST_CODE


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskCreateSerializer(data=request.data)

    if not serializer.is_valid():
        return generate_response(
            BAD_REQUEST_CODE,
            BAD_REQUEST,
            error_message=serializer.errors
        )

    serializer.save(created_by=request.user)

    return generate_response(
        CREATED_CODE,
        TASK_CREATED_SUCCESSFULLY,
        serializer.data
    )

