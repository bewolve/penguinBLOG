from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


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


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
