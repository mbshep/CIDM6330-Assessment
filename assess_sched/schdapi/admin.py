from django.contrib import admin
from .models import Assessment, Sched, Assessor

# Register your models here.
admin.site.register(Assessment)
admin.site.register(Sched)
admin.site.register(Assessor)
