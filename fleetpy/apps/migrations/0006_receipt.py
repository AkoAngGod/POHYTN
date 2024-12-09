# Generated by Django 5.1 on 2024-12-01 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField()),
                ('rental_days', models.IntegerField()),
                ('total_rent', models.FloatField()),
                ('payment_amount', models.FloatField()),
                ('balance', models.FloatField()),
                ('transaction_number', models.CharField(max_length=100, unique=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.driver')),
            ],
        ),
    ]
