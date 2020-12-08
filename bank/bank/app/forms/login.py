from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Custom login form
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control', 'maxlength': '150'})
        self.fields['password'].widget=forms.PasswordInput()
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
