from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path, include
from core import views
from courses.settings import DEBUG, MEDIA_ROOT, MEDIA_URL
from core.views import *

urlpatterns = [
    path("registration/", views.RegistrationView.as_view()),
    path("authorization/", LoginView.as_view(template_name="authorization.html")),
    path('admin/', admin.site.urls),
    path('base/', views.BasesView.as_view(), ),
    path('summernote/', include('django_summernote.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('profile/', views.ProfileView.as_view()),
    path('', views.IndexView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('courses/', views.CourseByCategoryView.as_view()),
    path('course/<int:pk>/', views.CourseView.as_view()),
    path('course/<int:pk>/students/', views.StudentShowView.as_view()),
    path('course/<int:pk_course>/lecture/<int:pk_lecture>', views.LectureView.as_view()),
    path('payment-charge/<int:pk>', views.ChargeView.as_view()),
    path('add-lecture/', views.AddLectureView.as_view()),
    path('course/<int:pk>/students/', views.StudentShowView.as_view()),
    path('add-homework/', views.AddHomeworkView.as_view()),
    path('homework/<int:pk_homework>/eval/', views.EvaluateHomework.as_view()),
    path('homework/<int:pk_homework>/pass/', views.PassHomework.as_view()),
    path('course/<int:pk>/students/<int:pk_student>', views.StudentProfileView.as_view()),
    path('profile/<int:pk>/edit/', views.EditProfileView.as_view()),


    path("reset-password/", views.CustomPasswordResetView.as_view(), name='reset-password'),
    path("reset-password-send/", views.CustomPasswordResetDoneView.as_view(), name='password-reset-done'),
    path("reset-password-complete/", views.CustomPasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path("reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(), name='password-reset-confirm')

    # path('reset-password/', views.CustomPasswordResetView.as_view(), name='reset-password'),
    # path('reset-password-send/', views.CustomPasswordResetDoneView.as_view(), name='reset-password-done'),
    # path('reset-password-complete', views.CustomPasswordResetCompleteView.as_view(), name='reset-password-complete'),
    # path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='reset-password-confirm'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
