import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import logging
from .serializers import TaskCreateSerializer
from resources.common_function import generate_response
from resources.message import TASK_CREATED_SUCCESSFULLY, BAD_REQUEST,CREATED_CODE,BAD_REQUEST_CODE,SUCCESS_CODE,DATA_RETRIEVED_SUCCESSFULLY,TASK_ALREADY_EXITS,INTERNAL_SERVER_ERROR
from .serializers import TaskListSerializer,TaskStatusUpdateSerializer

from .models import Task
from rest_framework.pagination import PageNumberPagination
logger = logging.getLogger(__name__)


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
    try:
        queryset = Task.objects.filter(is_deleted=False)
        status = request.query_params.get('status')
        assigned_to = request.query_params.get('assigned_to')
        if status:
            queryset = queryset.filter(status=status)
        if assigned_to:
            queryset = queryset.filter(assiged_to_id=assigned_to)
        paginator = TaskPagination()
        paginated_qs = paginator.paginate_queryset(queryset, request)
        serializer = TaskListSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        print("eeeeeeeeeeee",e)
        logger.exception(f"Error in list_tasks: {e}")
class TaskPagination(PageNumberPagination):
    page_size = 2            
    page_size_query_param = 'page_size'

    
@api_view(['POST'])
def update_task_status(request):

    try:
        payload = request.data
        task_id = payload.get("task_id")
        status = payload.get("status")
        user = request.user

        serializer = TaskStatusUpdateSerializer(data=payload)
        if not serializer.is_valid():
            logger.warning(f"Invalid data: {serializer.errors}")
            return generate_response(
                success=False,
                message="Invalid data",
                data=serializer.errors,
                status_code=400
            )
        task = Task.objects.get(id=task_id, is_deleted=False)
        serializer.update(task, {"status": status}, updated_by=user)
        logger.info(f"Task {task_id} updated by user {user.id}")

        task_data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "assigned_to": task.assigned_to.id if task.assigned_to else None,
            "updated_by": task.updated_by.id if task.updated_by else None,
            "updated_at": task.updated_at,
            "is_deleted": task.is_deleted
        }

        return generate_response(True, "Task updated successfully", task_data)

    except Task.DoesNotExist:
        logger.warning(f"Task {task_id} not found")
        return generate_response(False, "Task not found", 404)

    except Exception as e:
        logger.exception(f"Error updating task {task_id}: {e}")
        return generate_response(False, INTERNAL_SERVER_ERROR, 500)