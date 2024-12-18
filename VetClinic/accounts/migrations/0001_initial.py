# Generated by Django 5.1.2 on 2024-11-16 13:07

import VetClinic.accounts.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists!'}, help_text='The username should consist of uppercase and lowercase letters, numbers, and ./-/_ characters only', max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'Username should be at least 3 characters long'), VetClinic.accounts.validators.UsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='last name')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='country')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='city')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='phone number')),
                ('is_vet', models.BooleanField(default=False, verbose_name='veterinarian')),
            ],
        ),
    ]
