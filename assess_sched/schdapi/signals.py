import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimpleScheduleConsumer, SimpleAssessmentConsumer, SimpleAssessorConsumer
from .models import Assessment, Sched, Assessor

channel_layer = get_channel_layer()


# making sense of this example:
# - save_assessment is the receiver function
# - Assessment is the sender and post_save is the signal.
# - Use Case: Everytime an Assessment is saved, the save_profile function will be executed.
def log_assessment_to_csv(sender, instance, **kwargs):
    print("Assessment signal: CSV")

    file = Path(__file__).parent.parent / "schdarch" / \
        "domain" / "created_log.csv"
    print(f"Writing to {file}")

    # the with statement takes advantate of the context manager protocol: https://realpython.com/python-with-statement/#the-with-statement-approach
    # for reference, here is how open() works: https://docs.python.org/3/library/functions.html#open
    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                instance.id,
                instance.lab_id,
                instance.timeframe,
                instance.man_days,
                instance.notes,
                instance.type,
            ]
        )


def send_assessment_to_channel(sender, instance, **kwargs):
    print("Assessment signal: Channel")
    print(f"Sending Assessment to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "assessments-add", {"type": "print.assessment", "data": instance.notes}
    )


# connect the signal to this receiver
post_save.connect(log_assessment_to_csv, sender=Assessment)
post_save.connect(send_assessment_to_channel, sender=Assessment)


# can add more examples of saving an assessor and a schedule
