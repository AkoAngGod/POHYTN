# Generated by Django 5.1 on 2024-12-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
