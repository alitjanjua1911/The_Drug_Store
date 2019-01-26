from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, comit=True):
        user=super(RegistrationForm, self).save(comit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        if comit:
            user.save()

        return user


