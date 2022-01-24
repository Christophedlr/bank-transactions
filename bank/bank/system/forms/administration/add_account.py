from django.forms import ModelForm, ChoiceField
from bank.app.models import User
from bank.system.models import Account


class AdminAddAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminAddAccountForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

        self.fields['currency'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 10}
        )

        self.fields['decimal'].widget.attrs.update(
            {'class': 'form-control', 'min': 2, 'max': 8}
        )

        self.fields['user'].widget.attrs.update(
            {'class': 'form-control'}
        )

    class Meta:
        model = Account
        fields = ('name', 'currency', 'decimal', 'user')
