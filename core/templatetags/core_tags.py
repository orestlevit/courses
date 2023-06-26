from django import template
from django.db.models import Avg

from core.models import Lecture, HomeworkStudentDone

register = template.Library()


@register.filter(name="split")
def get_code(url):
    return url.split("/")[-1]


@register.filter(name="width")
def get_width(id_course, user):
    lectures = Lecture.objects.filter(course_id=id_course)
    lectures_count = lectures.count()
    percent = 0.0

    if lectures_count:
        percent = lectures.filter(lecture_finished__course=id_course,
                                  lecture_finished__username=user).count() / lectures_count * 100

    return percent


@register.filter(name="avg")
def get_avg(id_course, user):
    homework = HomeworkStudentDone.objects.filter(homework__lecture__course__id=id_course, user__username=user).aggregate(Avg("mark"))

    if homework.get("mark__avg"):
        return homework.get("mark__avg")
    else:
        return 0
