# by me
from .models import Profile

# by default
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms 

# inherit from UserCreationForm 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']

        # (case-insensitive) =>
        #  to make zeinab@gmail.com = ZEINAB@gmail.com or any combination of lower and uppercase
        email = email.lower()
        cleaned_data['email'] = email  
        
        # use email__iexact -> if found data in database that don't converted to lower
        if User.objects.filter(email=email).exists():
            self.add_error('email', "This email is already in use. Please use a different email address.")
            
        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'gender', 'headline', 'image']