

from django.contrib.auth import get_user_model
from django.utils import timezone

from core.models import Role, Lecture
from courses.celery import app


@app.task()
def check_courses():
    role = Role.objects.get(title__contains="Student")
    students = get_user_model().object.filter(role=role)

    for student in students:
        for course in student.course.all():
            if course.date_end < timezone.now():
                course.is_enabled = False
                course.course_finished.add(student)
                for lecture in Lecture.objects.filter(course=course):
                    student.lecture_finished.add(lecture)
                    student.save()
            course.save()