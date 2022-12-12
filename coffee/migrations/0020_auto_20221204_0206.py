# Generated by Django 3.2.16 on 2022-12-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0019_auto_20221124_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dis_discount',
            field=models.BooleanField(default=False, verbose_name='на главную'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False, verbose_name='есть скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(default='999', verbose_name='старая цена'),
        ),
    ]
