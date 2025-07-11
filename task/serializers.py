from rest_framework import serializers

from task.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'members',
        ]



class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'owner',
            'members',
        ]




# task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project',
        ]

