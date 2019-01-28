from django import forms
from django.forms import ModelForm
from .models import blogComments


class commentsForm(ModelForm):
    class Meta:
        model=blogComments
        exclude=()