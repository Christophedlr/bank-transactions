from django.forms import ModelForm
from bank.system.models import Account


class AddAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddAccountForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

        self.fields['currency'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 10}
        )

        self.fields['decimal'].widget.attrs.update(
            {'class': 'form-control', 'min': 2, 'max': 8}
        )

    class Meta:
        model = Account
        fields = ('name', 'currency', 'decimal')
