# Generated by Django 3.2.16 on 2022-11-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_product_full_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, verbose_name='Сжатое описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_desc',
            field=models.TextField(blank=True, verbose_name='Полное описание'),
        ),
    ]
