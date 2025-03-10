
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

def register_view(req):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(req, 'accounts/register.html', context)