from django.forms import ModelForm
from bank.system.models import Account


class AddAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddAccountForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

    class Meta:
        model = Account
        fields = ('name',)
