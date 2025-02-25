from .forms import RegisterForm, LoginForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.urls import reverse 
from django.views import View



def register_view(req):
    form = RegisterForm()
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            messages.success(req, 'Account created successfully')
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            return redirect('login')

    context={
        'title':'Register',
        'form': form,
    }
    return render(req, 'register.html', context)



# note can't make the view name -> login because it cause conflict with the built-in login function
def login_view(req):
    form = LoginForm()
    error_message = ''
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user,)
                messages.success(req, "Logged in successfully!")
                return redirect('post_list')
            else:
                error_message = 'Invalid username or password'
    context={
        'title':'Login',
        'form': form,
        'error_message': error_message,
    }
    return render(req, 'login.html', context)