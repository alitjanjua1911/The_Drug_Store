from django.shortcuts import render
from .models import slider
from blogs.models import Blog
from django.views.generic import TemplateView
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super(index, self).get_context_data(**kwargs)
        context['slider_model']=slider.objects.all()
        context['blogs_model']=Blog.objects.all()
        return context