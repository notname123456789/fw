# Generated by Django 3.2.16 on 2022-11-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0011_auto_20221108_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.TextField(blank=True, verbose_name='описание заказа'),
        ),
    ]