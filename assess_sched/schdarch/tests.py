from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from schdapi.models import Assessment, Assessor, Sched
from schdarch.domain.model import DomainAssessment
from schdarch.services.commands import (
    AddAssessmentCommand,
    ListAssessmentsCommand,
    DeleteAssessmentCommand,
    EditAssessmentCommand,
    #     GetAssessmentCommand,
)


class TestCommands(TestCase):
    def setUp(self):
        right_now = localtime().date()

        self.domain_assessment_1 = DomainAssessment(
            id=45,
            lab_id="ELP-045",
            timeframe="Fall",
            man_days=1,
            notes="new reloc",
            type="reloc",
        )

        self.domain_assessment_2 = DomainAssessment(
            id=46,
            lab_id="ELP-046",
            timeframe="Spring",
            man_days=2,
            notes="new pre",
            type="pre",
        )

    def test_command_add(self):
        add_command = AddAssessmentCommand()
        add_command.execute(self.domain_assessment_1)

        # run checks
        # one object is inserted
        self.assertEqual(Assessment.objects.count(), 1)

        # that object is the same as the one we inserted
        self.assertEqual(Assessment.objects.get(
            id=45).notes, self.domain_assessment_1.notes)

    def test_command_delete(self):
        # make sure there is a assessment to delete
        add_command = AddAssessmentCommand()
        add_command.execute(self.domain_assessment_2)
        # now lets try to delete it
        delete_command = DeleteAssessmentCommand()
        delete_command.execute(self.domain_assessment_2)

        # run checks

        # the item added has been deleted
        self.assertEqual(Assessment.objects.count(), 0)

    def test_command_list(self):
        # get two assessments into the database
        add_command = AddAssessmentCommand()
        add_command.execute(self.domain_assessment_1)
        add_command.execute(self.domain_assessment_2)
        list_command = ListAssessmentsCommand()
        list_command.execute(self.domain_assessment_2)

        # run checks

        # two objects are inserted
        self.assertEqual(Assessment.objects.count(), 2)

    def test_command_edit(self):

        add_command = AddAssessmentCommand()
        add_command.execute(self.domain_assessment_1)

        # just modify
        self.domain_assessment_1.notes = "This is not new"

        # going to try AddAssessmentCommand here since technically add and edit are the same Django command
        edit_command = AddAssessmentCommand()
        edit_command.execute(self.domain_assessment_1)

        # run checks
        # one object is inserted
        self.assertEqual(Assessment.objects.count(), 1)

        # that object is the same as the one we inserted
        self.assertEqual(Assessment.objects.get(
            id=45).notes, "This is not new")
