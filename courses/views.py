from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Lesson


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwards):
        ctx = super(HomePage, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwards):
        ctx = super(CourseDetailPage, self).get_context_data(**kwards)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')

        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'
