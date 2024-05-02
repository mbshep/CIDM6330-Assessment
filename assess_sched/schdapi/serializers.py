from .models import Assessment, Sched, Assessor
from django.contrib.auth.models import User
from rest_framework import serializers


class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assessment
        fields = ("id", "lab_id", "timeframe", "man_days", "notes", "type")


class AssessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assessor
        fields = ("id", "fname", "lname")


class SchedSerializer(serializers.HyperlinkedModelSerializer):
    assessment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Assessment.objects.all()
    )
    assessor = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Assessor.objects.all()
    )

    class Meta:
        model = Sched
        fields = ("assessment", "assessor")
