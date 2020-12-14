from django.shortcuts import render
from django.shortcuts import redirect

from bank.system.forms.add_account import AddAccountForm
from bank.system.forms.add_transaction import AddTransactionForm
from bank.system.forms.add_category import AddCategoryForm
from bank.system.models import Account, Category


def index(request):
    accounts = Account.objects.filter(user=request.user)

    return render(request, 'system/list.html', context={'accounts': accounts})


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


def add_transaction(request, id):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)

            account = Account.objects.filter(id=id)[0]

            if account:
                transaction.account = account
                transaction.save()

            return redirect('index_system')

    form = AddTransactionForm()

    return render(request, 'system/add_transaction.html', context={'form': form})


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)

        if form.is_valid():
            form.save()

            if request.GET:
                return redirect(request.GET.get('next', ''))

    form = AddCategoryForm()

    return render(request, 'system/add_category.html', context={'form': form})
