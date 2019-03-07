from multiprocessing import Value

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))