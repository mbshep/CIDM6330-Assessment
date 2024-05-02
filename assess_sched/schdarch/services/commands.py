"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC, abstractmethod
from datetime import datetime
# from injector import Injector, inject
import pytz

import requests
from django.db import transaction

from schdapi.models import Assessment, Assessor, Sched
from schdarch.domain.model import DomainAssessment  # , DomainAssessor, DomainSched
# DomainAssessor and DomainSched have not been added to schdarch.domain.model yet


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


class AddAssessmentCommand(Command):
    """
    Using the django orm and transactions to add a Assessment
    """


"""
    @inject
    def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
        self.now = now
"""


def execute(self, data: DomainAssessment):
    assessment = Assessment(
        data.id, data.lab_id, data.timeframe, data.man_days, data.notes, data.type)
#        assessment.timestamp = self.now

    # again, we skip the ouw with django's transaction management
    with transaction.atomic():
        assessment.save()


class GetAssessmentCommand(Command):
    """
    Using the django orm and transactions to add a Assessment
    """

    def execute(self, data: int):
        return Assessment.objects.get(id=data).to_domain()


class ListAssessmentsCommand(Command):
    """
    swapping in Django ORM for the database manager
    """

    def __init__(self, order_by="id"):
        self.order_by = order_by

    def execute(self, data=None):
        return Assessment.objects.all().order_by(self.order_by)


class DeleteAssessmentCommand(Command):
    """
    Using the django ORM to delete a Assessment
    """

    def execute(self, data: DomainAssessment):
        assessment = Assessment.objects.get(url=data.url)
        with transaction.atomic():
            assessment.delete()


class EditAssessmentCommand(Command):
    """
    Using the django ORM to update a Assessment
    """

    def execute(self, data: DomainAssessment):
        assessment = Assessment.update_from_domain(data)
        with transaction.atomic():
            assessment.save()
