# Generated by Django 3.1.4 on 2020-12-14 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 14, 11, 48, 47, 480330)),
        ),
    ]
