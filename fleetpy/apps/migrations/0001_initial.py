# Generated by Django 5.1 on 2024-11-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('middlename', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('role', models.CharField(choices=[('admin', 'user')], default='user', max_length=10)),
                ('status', models.CharField(choices=[('active', 'inactive')], default='inactive', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
