from rest_framework import viewsets, mixins
from rest_framework.views import exception_handler

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "name"


def magpy_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response.status_code == 400:
        response.data = {"error": "One or more packages doesn't exist"}
    return response
