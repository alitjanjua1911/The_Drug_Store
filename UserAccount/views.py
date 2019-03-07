from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        user_form=UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            model = User.objects.latest('id')
            model.email=request.POST['email']
            model.first_name=request.POST['first_name']
            model.last_name=request.POST['last_name']
            model.save()
            messages.success(request, "Successfully registered")
            return redirect(reverse('login'))
        else:
            messages.success(request, "Username is already registered. try another one")
            return redirect(reverse('register'))

    else:
        user_form=UserCreationForm()
        args={'user_form':user_form}
        return render(request, 'signup.html',args)