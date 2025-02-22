from .forms import EmailPostForm, RegisterForm, LoginForm
from .models import Post

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.urls import reverse 
from django.views import View



def post_list(req):
    posts = Post.published.all()
    paginator = Paginator(posts, 3) 
    page_number = req.GET.get('page', '1') # as req.GET.get('page') returns a string
    error_message =''

    try:
        page_number = int(page_number) 
        if page_number < 1:
            error_message = 'Page number must be greater than 0'
        elif page_number > paginator.num_pages:
            error_message = 'Page number must be less than or equal to the total number of pages'
    except ValueError:
        error_message = 'Page number must be an integer'
        
    if error_message :
        return render(req, 'error.html', {'error_message': error_message})

    posts = paginator.get_page(page_number)
    context = {
        'page': page_number,
        'posts': posts,
        'total_pages': paginator.num_pages,
    }
    return render(req, 'posts.html', context)


def post_details(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(req, 'posts.html', context)


def post_share(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    sent = False
    if req.method == 'POST':
        form = EmailPostForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = req.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read \'{post.title}\' --- '{cd['subject']}' "
            message = f"Read \'{post.title}\' at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['email_to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(req, 'post_share.html', context)



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