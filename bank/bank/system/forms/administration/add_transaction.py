from django.forms import ModelForm, ChoiceField, Select
from bank.app.models import User
from bank.system.models import Transaction


class AdminAddTransactionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminAddTransactionForm, self).__init__(*args, **kwargs)

        CHOICES= (
            (0, 'Débit'),
            (1, 'Crédit'),
        )

        self.fields['type'] = ChoiceField(widget=Select, choices=CHOICES)

        self.fields['label'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

        self.fields['date'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

        self.fields['type'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 10}
        )

        self.fields['categories'].widget.attrs.update(
            {'class': 'form-control'}
        )

    class Meta:
        model = Transaction
        fields = ('label', 'date', 'type', 'account', 'categories')
