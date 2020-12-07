from django import forms
from django.forms import ModelForm
from bank.app.models import User


class LoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget=forms.PasswordInput()
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'password']
