from rest_framework import viewsets

from account.permissions import  MemberTaskPermission, AssignedPermission
from task.models import Task
from task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [MemberTaskPermission()]
        elif self.action in ['create', 'update', 'partial_update']:
            return [AssignedPermission()]

        return self.get_permissions()

