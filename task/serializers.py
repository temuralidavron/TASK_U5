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
    # pr_name=serializers.SerializerMethodField()
    # user=serializers.SerializerMethodField()
    pro=serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project',
            'pro'
            # 'pr_name',
            # 'user'
        ]
    #
    # def get_pr_name(self, obj):
    #     project=obj.project
    #     if project:
    #         name=project.name
    #         return name
    #     return None
    #
    # def get_user(self,obj):
    #     project=obj.project
    #     if project:
    #         user=project.owner
    #         if user:
    #             return user.username




