from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.task_view.project import ProjectViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet,basename='pro')
urlpatterns = [
    path('',include(router.urls))
]