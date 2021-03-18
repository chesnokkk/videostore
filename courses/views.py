from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    contex_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwards):
        ctx = super(HomePage, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница сайта'
        return ctx
    
