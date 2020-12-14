from datetime import datetime
from django.db import models
from bank.app.models import User


# Accounts of user
class Account(models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'bank_account'
        verbose_name = 'Compte bancaire'
        verbose_name_plural = 'Comptes bancaire'

    def __str__(self):
        return "%s" % self.name


# Category of transaction
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = 'bank_category'
        verbose_name = 'Catégorie de transactions'
        verbose_name_plural = 'Catégories de transactions'


# Transaction of account
class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type = models.SmallIntegerField(default=1) # 0 = Debit, 1 = Credit
    label = models.CharField(max_length=50, null=False)
    amount = models.FloatField(null=False, default=0)
    date = models.DateTimeField(null=False, blank=True, default=datetime.now())

    def __str__(self):
        return "%s" % self.label

    class Meta:
        db_table = 'bank_transaction'
        verbose_name = 'Transaction bancaire'
        verbose_name_plural = 'Transactions bancaires'
