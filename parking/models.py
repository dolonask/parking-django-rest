from django.db import models

from datetime import datetime


# Create your models here.

statuses = (('OPEN','Открытая'),('CLOSED', 'Закрытая'), ('RUN', 'Списанная'))


class Tariff(models.Model):
    name = models.CharField("Название", max_length=100)
    start_date = models.DateTimeField("Дата начала действия", auto_now_add=True)
    end_date = models.DateTimeField("Дата завершения действия", default=datetime(2999, 12, 31))

    def __str__(self):
        return self.name


class TariffDetail(models.Model):
    hours = models.DecimalField("Время", max_digits=5, decimal_places=2)
    price = models.DecimalField("Стоимость", max_digits=5, decimal_places=2)
    tariff = models.ForeignKey(Tariff, on_delete=models.DO_NOTHING)


class OperatingDay(models.Model):
    start_date = models.DateTimeField("Дата начала действия", auto_now_add=True)
    end_date = models.DateTimeField("Дата завершения действия")


class Operation(models.Model):
    car_number = models.CharField("Номер автомобиля", max_length=20)

    add_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    edit_date = models.DateTimeField("Дата редактирования", auto_now=True)

    start_date = models.DateTimeField("Время заезда")
    end_date = models.DateTimeField("Время выезда")

    status = models.CharField("Статус операции", max_length=50, choices=statuses)
