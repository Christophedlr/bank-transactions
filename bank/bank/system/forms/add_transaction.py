from django import forms
from bank.system.models import Category, Transaction


class AddTransactionForm(forms.ModelForm):
    CHOICES= (
        (0, 'Débit'),
        (1, 'Crédit'),
    )

    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    category = forms.ModelChoiceField(queryset=Category.objects.order_by('name'))

    class Meta:
        model = Transaction
        fields = ('label', 'amount', 'type', 'category')
