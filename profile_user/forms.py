from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "col-md-12"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "col-md-12"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "col-md-12"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "col-md-12"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "col-md-12"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "col-md-12"}))
