from django.shortcuts import render
from django.shortcuts import redirect

from bank.system.forms.add_account import AddAccountForm


def index(request):
    return render(request, 'system/list.html', context={})


# Create new account
def add_account(request):
    if request.method == 'POST':
        form = AddAccountForm(request.POST)

        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()

            return redirect('index_system')

    form = AddAccountForm()

    return render(request, 'system/add_acount.html', context={'form': form})
