from django import forms
from django.contrib.auth.forms import UserCreationForm

from bank.app.models import User


# Custom register form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length="254", required=True, label="Adresse e-mail")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ("username","password1", "password2", "email")
