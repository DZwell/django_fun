from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extenstion = provider.split('.')
        if not extenstion == 'edu':
            raise forms.ValidationError("Please use a valid .edu email address")
        return email


