from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField( 
        max_length=25,
        label='Your Name',

    )
    email_from = forms.EmailField(
        label='Your Email',
    )
    email_to = forms.EmailField(
        label='Recipient Email',
    )

    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )

    def sendEmail(self):
        return f'Email sent from "{self.cleaned_data.get('email_from')}" ({self.cleaned_data.get('name')})\
        to "{self.cleaned_data.get('email_to')}" <br> with message {self.cleaned_data.get('comments')} '

