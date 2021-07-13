# Generated by Django 3.2.5 on 2021-07-13 03:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperatingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала действия')),
                ('end_date', models.DateTimeField(verbose_name='Дата завершения действия')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=20, verbose_name='Номер автомобиля')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('status', models.CharField(choices=[('OPEN', 'Открытая'), ('CLOSED', 'Закрытая'), ('RUN', 'Списанная')], max_length=50, verbose_name='Статус операции')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала действия')),
                ('end_date', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 0, 0), verbose_name='Дата завершения действия')),
            ],
        ),
        migrations.CreateModel(
            name='TariffDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Время')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parking.tariff')),
            ],
        ),
    ]
