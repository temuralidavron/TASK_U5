from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.task_view.project import ProjectViewSet
from task.task_view.task import TaskViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet,basename='pro')
router.register('task', TaskViewSet,basename='task')
urlpatterns = [
    path('',include(router.urls))
]