from django import forms


# Custom login form
class ProfileForm(forms.Form):
    email = forms.EmailField(max_length="254", required=True, label="Nouvelle adresse e-mail")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': '254'}
        )
