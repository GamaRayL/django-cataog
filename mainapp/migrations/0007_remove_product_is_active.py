# Generated by Django 4.2.5 on 2023-09-11 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
    ]