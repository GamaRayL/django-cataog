# Generated by Django 4.2.5 on 2023-10-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
    ]
