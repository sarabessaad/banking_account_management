# Generated by Django 5.1.2 on 2024-11-02 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cin', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('familyName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'clients',
                'ordering': ['email', 'cin'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('rib', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=15)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_app.client')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=9)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transactionType', models.CharField(choices=[('WTD', 'withdraw transaction'), ('DEP', 'deposit transaction'), ('TRAN', 'transfer transaction')], max_length=20)),
                ('transfer_to_account', models.CharField(blank=True, max_length=30, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.account')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
