from django.shortcuts import render
from django.views.generic import TemplateView
from .models import about, aboutCreativeTeam, aboutTestimonials
# Create your views here.



class aboutView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context=super(aboutView, self).get_context_data(**kwargs)
        context['about_model']=about.objects.filter(status=True)
        context['team_model']=aboutCreativeTeam.objects.filter(status=True)
        context['testimonial_model']=aboutTestimonials.objects.filter(status=True)

        return context
