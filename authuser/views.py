from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, ProfilePhotoForm

# Create your views here.


def registerUser(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "auth/signup.html", context)


def loginuser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "auth/login.html", context)


@login_required(login_url="login")
def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")


@login_required(login_url="login")
def change_profile_photo(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    form = ProfilePhotoForm(instance=profile)
    if request.method == "POST":
        form = ProfilePhotoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("userProfile")

    context = {"form": form}
    return render(request, "changepfp.html", context)
