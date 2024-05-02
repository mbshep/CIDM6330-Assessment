from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Assessment
from .views import AssessmentViewSet

# Create your tests here.
# test plan


class AssessmentTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.Assessment = Assessment.objects.create(
            id=10,
            lab_id="ELP-001",
            timeframe="Winter",
            man_days=1,
            notes="easy lab",
            type="Reassessment",
        )
        # print(f"Assessment id: {self.Assessment.id}")

        # the simple router provides the name 'Assessment-list' for the URL pattern: https://www.django-rest-framework.org/api-guide/routers/#simplerouter
        self.list_url = reverse("schdapi:assessment-list")
        self.detail_url = reverse(
            "schdapi:assessment-detail", kwargs={"pk": self.Assessment.id}
        )

    # 1. create a Assessment
    def test_create_Assessment(self):
        """
        Ensure we can create a new Assessment object.
        """

        # the full record is required for the POST
        data = {
            "id": 99,
            "lab_id": "ELP-099",
            "timeframe": "Summer",
            "man_days": 2,
            "notes": "Another lab",
            "type": "Initial"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Assessment.objects.count(), 2)
        self.assertEqual(Assessment.objects.get(id=99).notes, "Another Lab")

    # 2. list Assessments
    def test_list_Assessments(self):
        """
        Ensure we can list all Assessment objects.
        """
        response = self.client.get(self.list_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["results"]
                         [0]["notes"], self.Assessment.notes)

    # 3. retrieve a Assessment
    def test_retrieve_Assessment(self):
        """
        Ensure we can retrieve a Assessment object.
        """
        response = self.client.get(self.detail_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["notes"], self.Assessment.notes)

    # 4. delete a Assessment
    def test_delete_Assessment(self):
        """
        Ensure we can delete a Assessment object.
        """
        response = self.client.delete(
            reverse("schdapi:Assessment-detail",
                    kwargs={"pk": self.Assessment.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Assessment.objects.count(), 0)

    # 5. update a Assessment
    def test_update_Assessment(self):
        """
        Ensure we can update a Assessment object.
        """
        # the full record is required for the POST
        data = {
            "id": 199,
            "lab_id": "ELP-199",
            "timeframe": "Fall",
            "man_days": 2,
            "notes": "A third lab",
            "type": "PreAssessment"
        }
        response = self.client.put(
            reverse("schdapi:Assessment-detail",
                    kwargs={"pk": self.Assessment.id}),
            data,
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data["notes"], "A third lab")

# can do additional tests on assessors and schedules
