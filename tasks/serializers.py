from rest_framework import serializers
from .models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    scan_part = serializers.CharField(
        source='description',
        required=False,
        allow_blank=True,
        allow_null=False  
    )

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False
    )
    
    class Meta:
        model = Task
        fields = [
            'title',
            'scan_part',
            'start_date',
            'end_date'
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

class TaskStatusUpdateSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(required=True)
    status = serializers.CharField(required=True, max_length=100)

    def validate_task_id(self, value):
        if not Task.objects.filter(id=value, is_deleted=False).exists():
            raise serializers.ValidationError("Task with this ID does not exist.")
        return value

    def update(self, instance, validated_data, updated_by=None):
        instance.status = validated_data.get('status', instance.status)
        if updated_by:
            instance.updated_by = updated_by
        instance.save()  
        return instance    