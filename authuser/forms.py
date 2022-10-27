from socket import fromshare
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)  # Required
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
