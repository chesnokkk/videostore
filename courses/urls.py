from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
]
