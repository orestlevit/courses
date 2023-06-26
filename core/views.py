import stripe
from allauth.account.views import PasswordResetView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView, TemplateView, DetailView, CreateView, UpdateView
from stripe.error import InvalidRequestError

from core.forms import RegistrationForm
from core.models import Bases, Course, Category, Lecture, Comment, ProfileUser, Homework, Subscription, \
    HomeworkStudentDone


class BasesView(ListView):
    model = Bases
    template_name = "base.html"


class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = "/authorization/"

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = "profile.html"


class IndexView(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = Course
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.role.title == "Student":
            categories = Category.objects.all()
            context.update({
                "categories": categories
            })
        return context

    def get_queryset(self):
        if self.request.user.role.title == "Teacher":
            return Course.objects.filter(student_course=self.request.user.id)
        else:
            return Course.objects.all().annotate(count=Count("student_course")).order_by("-count")


class CourseByCategoryView(LoginRequiredMixin, ListView):
    template_name = "includes/courses.html"
    model = Course

    def get_queryset(self):
        return Course.objects.filter(
            category_id=self.request.GET.get("category")
        ).annotate(
            count=Count("student_course")
        ).order_by("-count")


class CourseView(LoginRequiredMixin, DetailView):
    template_name = "course_detail.html"
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = Course.objects.filter(student_course__username=self.request.user)
        if Course.objects.get(title__contains=kwargs.get("object")) in courses:
            lectures = Lecture.objects.filter(course_id=kwargs.get("object").id)
            comments = Comment.objects.filter(course_id=kwargs.get("object").id)

            context.update({
                "lectures": lectures,
                "comments": comments,
            })
        else:
            context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    def post(self, request, *args, **kwargs):
        Comment.objects.create(
            message=request.POST.get("comment"),
            course_id=kwargs.get("pk"),
            user_id=request.user.id,
            is_approved=True
        )
        return redirect(request.META['HTTP_REFERER'])


class StudentShowView(LoginRequiredMixin, ListView):
    template_name = "studentbycourse.html"
    model = get_user_model()

    def get_queryset(self):
        users = get_user_model().objects.filter(course=self.kwargs.get("pk"))
        return users


class LectureView(LoginRequiredMixin, DetailView):
    model = Lecture
    pk_url_kwarg = "pk_lecture"
    template_name = "lecture_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homeworks = Homework.objects.filter(lecture_id=kwargs.get('object').id)
        context["homeworks"] = homeworks
        return context

    def post(self, request, *args, **kwargs):
        current_lecture = Lecture.objects.get(id=kwargs.get("pk_lecture"))
        if current_lecture in request.user.lecture_finished.all():
            request.user.lecture_finished.remove(
                kwargs.get("pk_lecture")
            )
        else:
            request.user.lecture_finished.add(
                kwargs.get("pk_lecture")
            )

        return redirect(request.META['HTTP_REFERER'])


stripe.api_key = settings.STRIPE_SECRET_KEY


class ChargeView(LoginRequiredMixin, TemplateView):
    template_name = "charge.html"

    def post(self, request, pk):
        course = Course.objects.get(id=pk)

        try:
            charge = stripe.Charge.create(
                amount=course.price * 100,
                currency='USD',
                description=f'Purchase {course.title}',
                source=request.POST['stripeToken']
            )
            subscription = Subscription.objects.create(
                payment_id=charge.id,
                payment_status=charge.status,
                payment_message=charge.outcome.seller_message,
                date=charge.created,
                course_id=pk,
                user_id=request.user.id,

            )
            if charge.status == 'succeeded':
                request.user.course.add(course)
            subscription.save()
            return render(request, "charge.html")
        except InvalidRequestError as e:
            print(e)
            return HttpResponse("Not availabe")


class PassHomework(TemplateView):
    template_name = "lecture_detail.html"

    def post(self, request, *args, **kwargs):
        HomeworkStudentDone.objects.create(
            user_homework=request.POST["homework"],
            homework_id=kwargs.get("pk_homework"),
            user_id=request.user.id
        )

        return redirect(request.META["HTTP_REFERER"])


class EvaluateHomework(TemplateView):
    template_name = "lecture_detail.html"

    def post(self, request, *args, **kwargs):
        homework = HomeworkStudentDone.objects.get(id=kwargs.get("pk_homework"))
        mark = request.POST.get("mark")
        homework.mark = mark
        homework.save()

        return redirect(request.META["HTTP_REFERER"])



class AddLectureView(LoginRequiredMixin, CreateView):
    template_name = "add_lecture.html"
    model = Lecture
    success_url = "/"
    fields = "__all__"

    def form_valid(self, form):
        form.save()
        return super(AddLectureView, self).form_valid(form)




class AddHomeworkView(LoginRequiredMixin, CreateView):
    model =  Homework
    template_name = "add_homework.html"
    success_url = "/"
    fields = "__all__"
    def form_valid(self, form):
        form.save()
        return super(AddHomeworkView, self).form_valid(form)



class StudentProfileView(LoginRequiredMixin,DetailView):
    model = get_user_model()
    template_name = "student_profile.html"
    pk_url_kwarg = "pk_student"


class EditProfileView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    template_name = "edit_profile.html"
    fields = ["first_name", "last_name", "username", "email", "avatar"]
    success_url = "/profile"




#                   FORGOT PASSWORD                 #
class CustomPasswordResetView(PasswordResetView):
    template_name = "reset_password.html"
    email_template_name = "reset_password_email.html"
    success_url = "/reset-password-send/"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "reset_password_send.html"



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "reset_password_confirm.html"
    success_url = "/reset-password-complete"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "reset_password_complete"


#                   FORGOT PASSWORD                 #