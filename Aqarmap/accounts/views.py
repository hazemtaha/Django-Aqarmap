from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import RegisterationForm, UserCreationFormset, LoginForm

# Create your views here.


def register(request):
    form = RegisterationForm(request.POST or None)
    if form.is_valid():
        reg_form = form.save(commit=False)
        reg_form.password = make_password(form.cleaned_data['password'])
        reg_formset = UserCreationFormset(
            request.POST, request.FILES, instance=reg_form)
        if reg_formset.is_valid():
            reg_form.save()
            reg_formset.save()
            # redirect to login or site main page
    else:
        reg_formset = UserCreationFormset(
            request.POST or None, instance=User())
    context = {
        "form": form,
        "formset": reg_formset,
    }
    return render(request, "accounts/registeration.html", context)


def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "accounts/registeration.html", {})

    return render(request, "accounts/login.html", {'form': form})
