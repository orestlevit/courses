from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

from core.models import *

for model in models:
    admin.site.register(model)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = [
        'payment_id',
        'user',
        'course',
        'payment_message',
        'payment_message',
        'date',
    ]


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                "username",
                "password"
            )
        }),
        ("Personal Info", {
            'fields': (
                "first_name",
                "last_name",
                "email",
                "avatar",
                "role",
                "course_finished",
                "lecture_finished",
                "course"
            )
        }),
        ("Permissions", {
            'fields': (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
        ("Important dates", {
            'fields': (
                "last_login",
                "date_joined"
            )
        })
    )


admin.site.register(ProfileUser, UserProfileAdmin)


class SummerNoteFields(SummernoteModelAdmin):
    summernote_fields = 'description'


summernote = [Course, Lecture, Homework, Comment]

for model in summernote:
    admin.site.register(model, SummerNoteFields)
