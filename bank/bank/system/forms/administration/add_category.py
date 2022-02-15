from django.forms import ModelForm
from bank.system.models import Category


class AdminAddCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminAddCategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'maxlength': 50}
        )

    class Meta:
        model = Category
        fields = ('name',)
