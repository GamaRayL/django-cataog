# Generated by Django 4.2.5 on 2023-09-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]
