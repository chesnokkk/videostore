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
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['course']).order_by('number')

        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'


    def get_context_data(self, *, object_list=None, **kwards):
        ctx = super(LessonDetailPage, self).get_context_data(**kwards)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        #print (lesson)

        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split('=')[1]
        return ctx
