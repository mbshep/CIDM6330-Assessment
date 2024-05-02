from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Assessment, Assessor, Sched
from .serializers import AssessmentSerializer, SchedSerializer, AssessorSerializer


# Create your views here.
class AssessmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assessments to be viewed or edited.
    """

    queryset = Assessment.objects.all().order_by("id")
    serializer_class = AssessmentSerializer


class SchedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = Sched.objects.all()
    serializer_class = SchedSerializer


class AssessorViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """

    queryset = Assessor.objects.all()
    serializer_class = AssessorSerializer
