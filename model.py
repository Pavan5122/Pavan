
from django.db import models

class User(models.Model):
    
    username = models.CharField(max_length=100)
  
from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email'] 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Validate user credentials and login
            # Redirect to dashboard or homepage
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
