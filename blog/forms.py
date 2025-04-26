from django import forms
from .models import Post


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


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['title', 'content', 'status']