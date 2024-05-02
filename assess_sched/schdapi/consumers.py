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


class SimpleAssessorConsumer(AsyncConsumer):
    async def print_assessor(self, message):
        print(f"WORKER: Assessor: {message['data']}")


class SimpleScheduleConsumer(AsyncConsumer):
    async def print_schedule(self, message):
        print(f"WORKER: Schedule: {message['data']}")
