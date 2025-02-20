# Generated by Django 5.1 on 2024-12-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_receipt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='credit',
            new_name='balance',
        ),
        migrations.AlterField(
            model_name='driver',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='total_rent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='total_rent',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
