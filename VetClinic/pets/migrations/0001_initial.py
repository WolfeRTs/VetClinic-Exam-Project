# Generated by Django 5.1.2 on 2024-11-18 13:59

import VetClinic.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[VetClinic.validators.CapitalFirstLetterValidator()], verbose_name='name')),
                ('species', models.CharField(max_length=50, verbose_name='species')),
                ('breed', models.CharField(blank=True, max_length=50, null=True, verbose_name='breed')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='sex')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('doctors', models.ManyToManyField(related_name='doctor_pets', to=settings.AUTH_USER_MODEL, verbose_name='doctors')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_pets', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('instructions', models.TextField(verbose_name='instructions')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='date updated')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medical_reports', to=settings.AUTH_USER_MODEL, verbose_name='doctor')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_reports', to='pets.pet', verbose_name='pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_neutered', models.BooleanField(default=False, verbose_name='neutered')),
                ('is_vaccinated', models.BooleanField(default=False, verbose_name='vaccinated')),
                ('last_vaccinated_at', models.DateTimeField(blank=True, null=True, verbose_name='last vaccination date')),
                ('last_external_deworming', models.DateTimeField(blank=True, null=True, verbose_name='last external deworming')),
                ('last_internal_deworming', models.DateTimeField(blank=True, null=True, verbose_name='last internal deworming')),
                ('pet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='pets.pet', verbose_name='pet')),
            ],
        ),
    ]