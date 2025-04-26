# by me
from .forms import UserRegisterForm, LoginForm, EditProfileForm


# built-in
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




def register_view(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, f'Account created for {form.cleaned_data["username"]} successfully')
            return redirect('login')
    else :
        form = UserRegisterForm()
        
    context = {
        'form': form,
        'title': 'Create an account',
    }
    return render(req, 'accounts/register.html', context)



def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                messages.success(req,f"logged in successfully to user {form.cleaned_data['username']}")
                login(req, user)
                if user.profile.need_to_complete_profile :
                    user.profile.need_to_complete_profile = False
                    user.profile.save()
                    return redirect('edit_profile')
                return redirect('home')
            else :
                form.add_error('username', 'username or password is incorrect')
                form.add_error('password', 'username or password is incorrect')
    else :
        form = LoginForm()

    context ={
        'form': form ,
        'title': "Login to your account",
    }
    return render(req, 'accounts/login.html', context)


def logout_view(req):
    logout(req)
    messages.success(req, 'Logged out successfully')
    return redirect('login')


@login_required
def profile_view(req):
    context={
        'title': f'{req.user} Profile',
    }
    return render(req, 'accounts/profile.html', context)




@login_required
def edit_profile_view(req):
    user = req.user
    profile = user.profile
    if req.method == 'POST':
        form = EditProfileForm(req.POST, req.FILES, instance=profile) 
        if form.is_valid():
            form.save()
            messages.success(req, 'Profile updated successfully')
            return redirect('profile') 
    else:
        form = EditProfileForm(instance=profile)

    context ={
        'title': f'Edit {user.username} profile',
        'form': form,
    }
    return render(req, 'accounts/edit_profile.html', context)