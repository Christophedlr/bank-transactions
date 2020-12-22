from django.shortcuts import render
from django.shortcuts import redirect

from bank.system.forms.add_account import AddAccountForm
from bank.system.forms.add_transaction import AddTransactionForm
from bank.system.forms.add_category import AddCategoryForm
from bank.system.models import Account, Category, Transaction


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


# Change account name
def change_account(request, id):
    account = Account.objects.get(id=id)
    form = AddAccountForm(request.POST or None, instance=account)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save()

            return redirect('index_system')

    return render(request, 'system/add_acount.html', context={'form': form, 'submit': 'Modifier'})


def delete_account(request, id):
    Account.objects.get(id=id).delete()

    return redirect('index_system')


def add_transaction(request, id):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)

            account = Account.objects.filter(id=id)[0]

            if account:
                transaction.account = account
                transaction.save()

            return redirect('list_transactions_system', id=id)

    form = AddTransactionForm()

    return render(request, 'system/add_transaction.html', context={'form': form, 'id': id})


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)

        if form.is_valid():
            form.save()

            if request.GET:
                return redirect(request.GET.get('next', ''))

    form = AddCategoryForm()

    return render(request, 'system/add_category.html', context={'form': form})


def list_transactions(request, id):
    account = Account.objects.filter(user=request.user).filter(id=id)[0]

    if not account:
        redirect('index_system')

    transactions = Transaction.objects.filter(account=account).order_by()

    return render(
        request,
        'system/list_transactions.html',
        context={
            'account': account,
            'transactions': transactions,
            'id': id
        }
    )
