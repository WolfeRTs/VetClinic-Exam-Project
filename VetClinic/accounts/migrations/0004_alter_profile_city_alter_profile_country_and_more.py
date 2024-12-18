# Generated by Django 5.1.2 on 2024-11-29 11:31

import VetClinic.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3, 'City should be at least 3 characters long'), VetClinic.validators.CapitalFirstLetterValidator()], verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3, 'Country should be at least 3 characters long'), VetClinic.validators.CapitalFirstLetterValidator()], verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(2, 'First name should be at least 2 characters long'), VetClinic.validators.CapitalFirstLetterValidator()], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Last name should be at least 2 characters long'), VetClinic.validators.CapitalFirstLetterValidator()], verbose_name='last name'),
        ),
    ]
