from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)  # Required
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("pfp",)
        labels = {"pfp": "Choose your profile photo"}
