# Generated by Django 3.2.16 on 2022-11-03 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
