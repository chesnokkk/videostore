from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Course, Lesson
from .forms import CreateForm
from django.contrib import messages
from django.core.exceptions import ValidationError


def create_course(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Курс {title} успешно добавлен')
            return redirect('/')

    else:
        form = CreateForm()

    return render(request,'courses/create_course.html', {'form':form})


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
