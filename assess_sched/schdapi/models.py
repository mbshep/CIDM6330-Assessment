from django.db import models

from schdarch.domain.model import DomainAssessment

# Create your models here.


class Assessment(models.Model):
    assess_types = {
        "Reassess": "rea",
        "Initial": "ini",
        "PreAssessment": "pre",
        "Relocation": "reloc",
    }
    id = models.IntegerField(primary_key=True)
    lab_id = models.CharField(max_length=10, null=False)
    timeframe = models.CharField(max_length=50)
    man_days = models.IntegerField()
    notes = models.TextField()
    type = models.CharField(choices=assess_types,
                            default="Reassess", max_length=50)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        app_label = "schdapi"

    # these methods are borrowed from P&G
    # it is not clear if they are needed as we are simply translating to and from pure Python
    # objects to Django models and back.
    @staticmethod
    def update_from_domain(domain_assessment: DomainAssessment):
        try:
            assessment = Assessment.objects.get(id=domain_assessment.id)
        except Assessment.DoesNotExist:
            assessment = Assessment(id=domain_assessment.id)

        assessment.id = domain_assessment.id
        assessment.lab_id = domain_assessment.lab_id
        assessment.timeframe = domain_assessment.timeframe
        assessment.notes = domain_assessment.notes
        assessment.man_days = domain_assessment.man_days
        assessment.type = domain_assessment.type
        assessment.save()

    def to_domain(self) -> DomainAssessment:
        b = DomainAssessment(
            id=self.id,
            lab_id=self.lab_id,
            timeframe=self.timeframe,
            man_days=self.man_days,
            notes=self.notes,
            type=self.type,
        )
        return b


'''
    technologies = {
        "Chemistry": "chem",
        "Micro": "micro",
        "WET": "wet",
        "Radiochemistry": "radchem",
        "Asbestos": "asb",
    }
'''


class Assessor(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=50)
#    techs = models.CharField(choices=technologies,
#                             default="Chemistry", max_length=15)


class Sched(models.Model):
    Assessment: models.ForeignKey(Assessment, on_delete=models.CASCADE)
    Assessor: models.ForeignKey(Assessor, on_delete=models.CASCADE)


# I started with this as a separate table but realized
# that is extra work at this point. Will hard code lab_id
# into the assessment table
class Lab(models.Model):
    technologies = {
        "Chemistry": "chem",
        "Micro": "micro",
        "WET": "wet",
        "Radiochemistry": "radchem",
        "Asbestos": "asb",
    }
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    techs = models.CharField(choices=technologies,
                             default="Chemistry", max_length=15)
    location = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
