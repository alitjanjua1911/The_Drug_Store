from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register')
]