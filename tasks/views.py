import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskCreateSerializer
from resources.common_function import generate_response
from resources.message import TASK_CREATED_SUCCESSFULLY, BAD_REQUEST,CREATED_CODE,BAD_REQUEST_CODE,SUCCESS_CODE,DATA_RETRIEVED_SUCCESSFULLY,TASK_ALREADY_EXITS
from .serializers import TaskListSerializer
from .models import Task


@api_view(['POST'])
def create_task(request):
    title = request.data.get('title')

  
    if Task.objects.filter(title=title, created_by=request.user).exists():
        return generate_response(
            BAD_REQUEST_CODE,
            TASK_ALREADY_EXITS
        )

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

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list_tasks(request):
    queryset = Task.objects.filter(is_deleted=False)

    serializer = TaskListSerializer(queryset, many=True)

    return generate_response(
        SUCCESS_CODE,
        DATA_RETRIEVED_SUCCESSFULLY,
        serializer.data
    )