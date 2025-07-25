from django.contrib.postgres.search import TrigramSimilarity
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from account.permissions import  MemberTaskPermission, AssignedPermission
from task.models import Task
from task.pagination import CustomPagination
from task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('project').only(
    'id', 'title', 'description', 'status', 'created_at', 'project__name'
)
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']
    pagination_class = CustomPagination

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'description']
    # permission_classes = [IsAuthenticated,]
    # authentication_classes = [TokenAuthentication,]


    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         return [MemberTaskPermission()]
    #     elif self.action in ['create', 'update', 'partial_update']:
    #         return [AssignedPermission()]
    #
    #     return [IsAuthenticated(),]

    # def get_queryset(self):
    #     search_query = self.request.query_params.get('search')
    #
    #     queryset = Task.objects.all()
    #
    #     if search_query:
    #         queryset = queryset.annotate(
    #
    #             similarity=TrigramSimilarity('title', search_query)
    #
    #         ).filter(similarity__gt=0.3).order_by('-similarity')
    #
    #     return queryset



