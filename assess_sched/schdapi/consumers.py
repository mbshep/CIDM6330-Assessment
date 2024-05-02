# python
import asyncio
import datetime
import json

# Django
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.generic.http import AsyncHttpConsumer

# Local
from schdapi.models import Assessment, Assessor, Sched

# It appeared in the final refactor that only the simple consumer
# was used so I only created that type here.


class SimpleAssessmentConsumer(AsyncConsumer):
    async def print_assessment(self, message):
        print(f"WORKER: Assessment: {message['data']}")


class AssessmentConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        # Get all assessments
        assessments = Assessment.objects.all()
        # Serialize the assessments
        data = json.dumps(
            [{"id": assessment.id, "lab_id": assessment.lab_id}
                for assessment in assessments]
        )
        # Send the serialized data as a JSON response
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    # Server-send event https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_assessment(self, assessment):
        # Serialize the bookmark
        data = json.dumps({"id": assessment.id, "lab_id": assessment.lab_id})
        # Send the serialized data as a JSON response
        await self.channel_layer.send(
            "assessments-add", {"type": "send.assessment", "data": data}
        )


class SimpleAssessorConsumer(AsyncConsumer):
    async def print_assessor(self, message):
        print(f"WORKER: Assessor: {message['data']}")


class SimpleScheduleConsumer(AsyncConsumer):
    async def print_schedule(self, message):
        print(f"WORKER: Schedule: {message['data']}")
