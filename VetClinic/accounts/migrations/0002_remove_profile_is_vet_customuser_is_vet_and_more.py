# Generated by Django 5.1.2 on 2024-11-16 15:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_vet',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_vet',
            field=models.BooleanField(default=False, verbose_name='veterinarian'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]