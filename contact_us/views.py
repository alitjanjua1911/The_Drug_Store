from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView
from .models import contact, contactMessages
from django.contrib import messages


def contacts(request):
    if request.method=="GET":
        contact_model = contact.objects.all()
        return render(request, 'contact-us.html', {'contact_model':contact_model})
    else:
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email_address') and request.POST.get('contact_subject') and request.POST.get('message'):
            _contact=contactMessages()
            _contact.senderName=request.POST.get('name')
            _contact.sender_email=request.POST.get('email_address')
            _contact.sender_phoneNo=request.POST.get('phone')
            _contact.msg_subject=request.POST.get('contact_subject')
            _contact.msg=request.POST.get('message')
            _contact.save()
            messages.success(request, 'Your message is successfully sent')
            return redirect(reverse('contact'))
            # return render(request, 'contact-us.html', {'flag':True})
        else:
            # return render(request, 'contact-us.html', {'flag': False})
            messages.success(request, 'Error in sending message')
            return redirect(reverse('contact'))
