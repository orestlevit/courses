import os

import celery as celery
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courses.settings ")

app = Celery("course")

app.config_from_object("django.conf:setting", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "check-course-every-1-day": {
        "task": "core.task.check_courses",
        "schedule": crontab(minute=0, hour=0)
    }
}