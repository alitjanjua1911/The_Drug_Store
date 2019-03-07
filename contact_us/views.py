from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView
from .models import contact, contactMessages
from django.contrib import messages

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def contacts(request):
    if request.method=="GET":
        contact_model = contact.objects.all()
        return render(request, 'contact-us.html', {'contact_model':contact_model})
    else:
        sender_name=request.POST.get('name')
        sender_phone=request.POST.get('phone')
        sender_email=request.POST.get('email_address')
        email_subject=request.POST.get('contact_subject')
        email_msg=request.POST.get('message')
        if sender_name and sender_phone and sender_email and email_subject and email_msg:
            _contact=contactMessages()
            _contact.senderName=sender_name
            _contact.sender_email=sender_email
            _contact.sender_phoneNo=sender_phone
            _contact.msg_subject=email_subject
            _contact.msg=email_msg
            try:
                send_mail(subject=email_subject, from_email="ali.official911@gmail.com", recipient_list=["ali.official1911@gmail.com"], message=email_msg, fail_silently=False)
                _contact.save()
                messages.success(request, 'Your message is successfully sent')
            except BadHeaderError:
                return HttpResponse("invalid header found")

            return redirect(reverse('contact'))
            # return render(request, 'contact-us.html', {'flag':True})
        else:
            # return render(request, 'contact-us.html', {'flag': False})
            messages.success(request, 'Error in sending message')
            return redirect(reverse('contact'))
