
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_view(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, f'Account created for {form.cleaned_data['username']} successfully')
            return redirect('home')
    else :
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(req, 'accounts/register.html', context)