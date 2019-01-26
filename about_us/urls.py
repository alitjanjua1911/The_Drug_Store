from django.urls import path
from . import views

urlpatterns=[
    path('', views.aboutView.as_view() , name='about')
]