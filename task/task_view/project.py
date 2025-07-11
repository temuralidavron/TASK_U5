from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from account.permissions import IsOwnerOrReadOnly, MembersPermission
from task.models import Project
from task.serializers import ProjectSerializer, ProjectCreateSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        elif self.action in ['list', 'retrieve']:
            return [MembersPermission()]
        return super().get_permissions()  # default permission agar yuqoridagilarga to‘g‘ri kelmasa

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Project.objects.all()
    #     return Project.objects.none()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
