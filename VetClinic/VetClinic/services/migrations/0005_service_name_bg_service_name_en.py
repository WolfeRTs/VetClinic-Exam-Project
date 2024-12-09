# Generated by Django 5.1.2 on 2024-12-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_servicecategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name_bg',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='name'),
        ),
    ]
