from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            Profile.objects.create(
                user=user,
                role=form.cleaned_data["role"]
            )

            login(request, user)

            return redirect("dashboard")

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("dashboard")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")