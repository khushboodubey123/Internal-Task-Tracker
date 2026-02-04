from rest_framework import serializers
from .models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'assigned_to'
        ]
        
class TaskListSerializer(serializers.ModelSerializer):
    assigned_to = serializers.CharField(
        source='assigned_to.username',
        read_only=True
    )
    created_by = serializers.CharField(
        source='created_by.username',
        read_only=True
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assigned_to',
            'created_by',
            'created_at',
            'updated_at'
        ]