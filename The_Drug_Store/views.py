from multiprocessing import Value

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse


def about(request):
    if request.method=='GET':
        return render(request, '../about_us/templates/about-us.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))