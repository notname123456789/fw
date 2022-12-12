# Generated by Django 3.2.16 on 2022-10-25 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ctg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Категория_внешней_фильтрации',
                'verbose_name_plural': 'Категории_внешней фильтрации',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SOME_NAME_THERE', max_length=200)),
                ('price', models.IntegerField(default='999')),
                ('amount', models.IntegerField(default='0')),
                ('desc', models.TextField(blank=True, verbose_name='FULL_DESCRIPTION')),
                ('image', models.ImageField(blank=True, upload_to='static\\media\\img')),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coffee.ctg')),
            ],
        ),
        migrations.CreateModel(
            name='another_product',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'Другие товары',
                'verbose_name_plural': 'Другие товары',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='cof',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'кофе',
                'verbose_name_plural': 'кофе',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='liq',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'Сироп',
                'verbose_name_plural': 'Сиропы',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='presents',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'Подарочные набор',
                'verbose_name_plural': 'Подарочные наборы',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='sweets',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'конфеты',
                'verbose_name_plural': 'конфеты',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='tea',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'чай',
                'verbose_name_plural': 'чаи',
            },
            bases=('coffee.product',),
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coffee.product')),
            ],
            options={
                'verbose_name': 'кофе',
                'verbose_name_plural': 'кофе',
            },
            bases=('coffee.product',),
        ),
    ]