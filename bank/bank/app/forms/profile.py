from django import forms
from django.core.validators import MinLengthValidator, RegexValidator, ValidationError


# Custom login form
class ProfileForm(forms.Form):
    email = forms.EmailField(max_length="254", required=True, label="Nouvelle adresse e-mail")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': '254'}
        )


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(
        max_length="128",
        required=True,
        label="Nouveau mot de passe",
        help_text="Le mot de passe doit faire 8 caractères minimum et, comporter des lettres & des chiffres",
        validators=[
            MinLengthValidator(8, "Votre mot de passe doit faire au moins 8 caractères"),
            RegexValidator('^(?=.*[\\d])(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$',
                           'Vous devez mélanger des lettres et des chiffres'),
        ],
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        max_length="128",
        required=True,
        label="Confirmation du nouveau mot de passe",
        validators=[
            MinLengthValidator(8, "Votre mot de passe doit faire au moins 8 caractères"),
            RegexValidator('^(?=.*[\\d])(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$',
                           'Vous devez mélanger des lettres et des chiffres'),
        ],
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': '128'}
        ),
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': '128'}
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password1', ValidationError('Les deux mots de passe ne correspondent pas'))
