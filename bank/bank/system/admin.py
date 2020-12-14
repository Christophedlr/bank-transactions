from django.contrib import admin

from bank.system.models import Category, Transaction, Account

admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Account)
