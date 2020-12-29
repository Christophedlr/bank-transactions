# Generated by Django 3.1.4 on 2020-12-29 13:07

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0005_auto_20201222_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(default='€', max_length=10, verbose_name='Monnaie'),
        ),
        migrations.AlterField(
            model_name='account',
            name='decimal',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(8)], verbose_name='Décimales'),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nom du compte'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 29, 14, 7, 46, 20978)),
        ),
    ]
