# Generated by Django 5.1 on 2024-12-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_rename_driver_firstname_receipt_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='vehicle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
