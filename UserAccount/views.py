from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
from django.urls import reverse

def login(request):
    # if request.method=="POST":
    #     m = User.objects.get(username=request.POST['username'])
    #     if m.password == request.POST['password']:
    #         request.session['user'] = m.username
    #         return redirect(reverse('index'))
    #     else:
    #         messages.error(request, 'Wrong username or password')
    # else:
    #     return render(request, 'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        user_form=UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('index'))

    else:
        user_form=UserCreationForm()
        args={'user_form':user_form}
        return render(request, 'signup.html',args)