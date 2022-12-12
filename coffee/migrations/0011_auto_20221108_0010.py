# Generated by Django 3.2.16 on 2022-11-07 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0010_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.IntegerField(max_length=4, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='coffee.product'),
        ),
    ]
