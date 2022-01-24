from django.contrib import admin

from bank.system.models import Category, Transaction, Account
from bank.administration.admin import AbstractAdministrationLinks


class AdministrationLinks(AbstractAdministrationLinks):
    def __init__(self):
        self.add_menu('Système')
        self.add_link('Système', 'Liste des comptes', 'admin_account_list')


class AccountAdmin(admin.ModelAdmin):
    model = Account

    list_display = ('name', 'currency', 'decimal')


admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Account, AccountAdmin)
