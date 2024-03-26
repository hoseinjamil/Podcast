from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You are logged in Now")
                return redirect('/')
            else:
                form.add_error("password", "username or password is not correct!")
    else:
        form = LoginForm()

    return render(request, "profile_user/user_login.html", {'form': form})


def is_strong_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    return True


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd["username"]).exists():
                form.add_error("username", "Email or phone number already exists")
            elif not is_strong_password(cd["password"]):
                form.add_error("password",
                               "Password must be at least 8 characters long and contain at least one digit, one uppercase letter, one lowercase letter, and one special character")
            elif cd["password"] != cd["password2"]:
                form.add_error("password2", "Passwords do not match")
            else:
                user = User.objects.create_user(username=cd["username"], email=cd["email"],
                                                password=cd["password"])
                login(request, user)
                messages.success(request, "You have created an account and logged in Now")
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('/')

    else:
        form = RegisterForm()
    return render(request, "profile_user/user_register.html", context={'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "You are logged out Now")
    return redirect('/')
