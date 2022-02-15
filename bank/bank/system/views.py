from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Sum

from bank.system.forms.add_account import AddAccountForm
from bank.system.forms.add_transaction import AddTransactionForm
from bank.system.forms.add_category import AddCategoryForm
from bank.system.forms.administration.add_account import AdminAddAccountForm
from bank.system.forms.administration.add_transaction import AdminAddTransactionForm
from bank.system.forms.administration.add_category import AdminAddCategoryForm

from bank.system.models import Account, Category, Transaction
from bank.app.models import User


def index(request):
    accounts = Account.objects.filter(user=request.user)

    return render(request, 'system/list.html', context={'accounts': accounts, 'account': AddAccountForm()})


# Create new account
def add_account(request):
    form = AddAccountForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()

            return redirect('index_system')

    return render(request, 'system/add_acount.html', context={'account': form})


# Change account name
def change_account(request, id):
    account = Account.objects.get(id=id)
    form = AddAccountForm(request.POST or None, instance=account)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save()

            return redirect('index_system')

    return render(request, 'system/add_acount.html', context={'form': form, 'submit': 'Modifier'})


def ajax_get_account(request, id):
    account = Account.objects.get(id=id)
    form = AddAccountForm(request.POST or None, instance=account)

    return render(request, 'system/forms/account.html', context={'account': form, 'submit': 'Modifier'})


def delete_account(request, id):
    Account.objects.get(id=id).delete()

    return redirect('index_system')


def add_transaction(request, id):
    form = AddTransactionForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            transaction = form.save(commit=False)

            account = Account.objects.filter(id=id)[0]

            if account:
                transaction.account = account
                transaction.save()
                transaction.categories.set(form.cleaned_data['categories'])

            return redirect('list_transactions_system', id=id)

    return render(request, 'system/add_transaction.html', context={'transaction': form, 'id': id})


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

    if request.GET.get('startdate') and request.GET.get('enddate'):
        transactions = Transaction.objects.filter(
            account=account, date__range=(request.GET.get('startdate'), request.GET.get('enddate'))
        ).order_by('-date')
    else:
        transactions = Transaction.objects.filter(account=account).order_by('-date')

    credit: float = 0
    debit: float = 0

    for transaction in transactions:
        if transaction.type == 1:
            credit += transaction.amount
        else:
            debit += -transaction.amount

    return render(
        request,
        'system/list_transactions.html',
        context={
            'account': account,
            'transactions': transactions,
            'id': id,
            'transaction': AddTransactionForm(),
            'credit': credit,
            'debit': -debit,
            'total': credit - (-debit),
        }
    )


def admin_account_list(request):
    accounts = Account.objects.all()

    return render(request, 'system/administration/account_list.html', {
        'accounts': accounts,
    })


def admin_account_change(request, id):
    account = Account.objects.get(id=id)
    form = AdminAddAccountForm(request.POST or None, instance=account)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save()

            return redirect('admin_account_list')

    return render(request, 'system/administration/forms/account_change.html', {
        'account': form,
        'submit': 'Modifier',
        'id': id,
    })


def admin_account_delete(request, id):
    Account.objects.get(id=id).delete()

    return redirect('admin_account_list')


def admin_account_add(request):
    form = AdminAddAccountForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()

            return redirect('admin_account_list')

    return render(request, 'system/administration/forms/add_acount.html', context={'account': form})


def admin_transaction_list(request):
    filter: dict = {}
    transactions: dict = {}

    if "account" in request.GET:
        filter['account'] = request.GET['account']

    if "user" in request.GET:
        filter['user'] = request.GET['user']

    if filter:
        transactions = Transaction.objects\
            .filter(account=filter['account'])\
            .filter(account__user=filter['user'])\
            .order_by('account', '-date')

    accounts = Account.objects.all().order_by('name')
    users = User.objects.all().order_by('username')

    return render(request, 'system/administration/transaction_list.html', {
        'transactions': transactions,
        'accounts': accounts,
        'users': users,
    })


def admin_transaction_change(request, id):
    transaction = Transaction.objects.get(id=id)
    form = AdminAddTransactionForm(request.POST or None, instance=transaction)

    if request.method == 'POST':
        if form.is_valid():
            account = form.save()

            return redirect('admin_transaction_list')

    return render(request, 'system/administration/forms/transaction_change.html', {
        'transaction': form,
        'submit': 'Modifier',
        'id': id,
    })


def admin_transaction_delete(request, id):
    Transaction.objects.get(id=id).delete()

    return redirect('admin_transaction_list')


def admin_category_list(request):
    categories = Category.objects.all()

    return render(request, 'system/administration/category_list.html', {
        'categories': categories,
    })


def admin_category_add(request):
    form = AdminAddCategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('admin_category_list')

    return render(request, 'system/administration/forms/add_category.html', context={'category': form})


def admin_category_change(request, id):
    category = Category.objects.get(id=id)
    form = AdminAddCategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('admin_category_list')

    return render(request, 'system/administration/forms/category_change.html', {
        'category': form,
        'submit': 'Modifier',
        'id': id,
    })


def admin_category_delete(request, id):
    Category.objects.get(id=id).delete()

    return redirect('admin_category_list')
