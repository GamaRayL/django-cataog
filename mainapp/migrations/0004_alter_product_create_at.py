# Generated by Django 4.2.5 on 2023-09-10 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0003_remove_product_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания'),
        ),
    ]
