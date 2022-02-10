from datetime import datetime
from django import forms
from bank.system.models import Category, Transaction


class AddTransactionForm(forms.ModelForm):
    CHOICES= (
        (0, 'Débit'),
        (1, 'Crédit'),
    )

    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.order_by('name'))
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Transaction
        fields = ('label', 'amount', 'type', 'categories', 'account', 'date')
