# Generated by Django 3.1.4 on 2020-12-04 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compte bancaire',
                'verbose_name_plural': 'Comptes bancaire',
                'db_table': 'bank_account',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Catégorie de transactions',
                'verbose_name_plural': 'Catégories de transactions',
                'db_table': 'bank_category',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(default=1)),
                ('label', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system.category')),
            ],
            options={
                'verbose_name': 'Transaction bancaire',
                'verbose_name_plural': 'Transactions bancaires',
                'db_table': 'bank_transaction',
            },
        ),
    ]
