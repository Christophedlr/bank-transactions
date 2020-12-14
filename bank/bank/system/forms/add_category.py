from django import forms
from bank.system.models import Category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
