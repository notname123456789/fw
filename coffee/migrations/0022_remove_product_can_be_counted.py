# Generated by Django 3.2.16 on 2022-12-06 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0021_auto_20221206_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='can_be_counted',
        ),
    ]
