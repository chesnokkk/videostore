from django.contrib import admin
from django.urls import path, include
from . import views as courseView
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [

    path('', courseView.HomePage.as_view(), name='home'),
    path('course/<slug>', courseView.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', courseView.LessonDetailPage.as_view(), name='lesson-detail'),
    path('create', courseView.create_course, name='create_course'),
]
