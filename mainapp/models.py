from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class LowerField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class EatingTime(models.Model):
    name = LowerField(verbose_name='Время еды', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mainapp_eatingtime'
        verbose_name = 'Время еды'
        verbose_name_plural = 'Время еды'


class FoodIntake(models.Model):
    e_time = models.ForeignKey(EatingTime, on_delete=models.PROTECT, verbose_name='Время питания')
    food = LowerField(verbose_name='Продукты', max_length=256)
    created_at = models.DateTimeField(verbose_name='Время записи', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user} / {self.e_time}'

    def get_absolute_url(self):
        return reverse('mainapp:food_intake_update', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'mainapp_foodintake'
        verbose_name = 'Прием еды'
        verbose_name_plural = 'Приемы еды'
        ordering = ('-created_at', )
