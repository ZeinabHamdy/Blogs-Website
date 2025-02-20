from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField( 
        max_length=25,
        label='Your Name',

    )
    email_to = forms.EmailField(
        label='Recipient Email',
    )
    subject = forms.CharField(
        max_length=100,
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )



class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='confirm_Password',
        widget=forms.PasswordInput(),
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        errors = {}
        if User.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists'
        if User.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'
        if password and confirm_password and password != confirm_password:
            errors['password'] = []
            errors['password'].append('Passwords do not match')
        if password and len(password) < 8:
            if 'password' not in errors:
                errors['password'] = []
            errors['password'].append('Password must be at least 8 characters')

        if errors:
            raise ValidationError(errors)
        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        label='Username',
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
    )
