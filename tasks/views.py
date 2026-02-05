import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskCreateSerializer
from resources.common_function import generate_response
from resources.message import TASK_CREATED_SUCCESSFULLY, BAD_REQUEST,CREATED_CODE,BAD_REQUEST_CODE,SUCCESS_CODE,DATA_RETRIEVED_SUCCESSFULLY,TASK_ALREADY_EXITS
from .serializers import TaskListSerializer
from .models import Task
from rest_framework.pagination import PageNumberPagination


@api_view(['POST'])
def create_task(request):
    title = request.data.get('title')
    if Task.objects.filter(title__iexact=title).exists():
        return generate_response(
            BAD_REQUEST_CODE,
            TASK_ALREADY_EXITS
        )

    serializer = TaskCreateSerializer(data=request.data)

    if not serializer.is_valid():
        print("serilizerrrrrr",serializer.errors)
        return generate_response(
            BAD_REQUEST_CODE,
            BAD_REQUEST,
            error_message=serializer.errors
        )
    print("about to save")
    task=serializer.save(created_by_id=1)
    print("dbbbbbbbbberrorrrrrrrr",task.id)

    return generate_response(
        CREATED_CODE,
        TASK_CREATED_SUCCESSFULLY,
        serializer.data
    )

@api_view(['GET'])
def list_tasks(request):
 
    queryset = Task.objects.filter(is_deleted=False)
    status = request.query_params.get('status')
    assigned_to = request.query_params.get('assigned_to')
    if status:
        queryset = queryset.filter(status=status)
    if assigned_to:
        queryset = queryset.filter(assigned_to_id=assigned_to)
    paginator = TaskPagination()
    paginated_qs = paginator.paginate_queryset(queryset, request)
    serializer = TaskListSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data)

class TaskPagination(PageNumberPagination):
    page_size = 2            
    page_size_query_param = 'page_size'