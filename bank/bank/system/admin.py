from django.contrib import admin

from bank.system.models import Category, Transaction, Account


class AccountAdmin(admin.ModelAdmin):
    model = Account

    list_display = ('name', 'currency', 'decimal')


admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Account, AccountAdmin)
