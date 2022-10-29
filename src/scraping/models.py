from django.db import models


class Film(models.Model):
    film_name = models.CharField(
        max_length=48,
        verbose_name='Название фильма'
    )
    film_id = models.IntegerField(
        verbose_name='id фильма на кинопоиске',
        unique=True
    )
    slug = models.CharField(
        max_length=48,
        blank=True,
        unique=True
    )
    
    class Meta:
        verbose_name = 'Название фильма'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.film_name


class Staff(models.Model):
    staff_role = models.CharField(
        max_length=48,
        verbose_name='Должность'
    )
    staff_name = models.CharField(
        max_length=48,
        verbose_name='Имя актера'
    )
    staff_id = models.IntegerField(
        verbose_name='Id человека на кинопоиске',
        unique=True
    )
    slug = models.CharField(
        max_length=48,
        blank=True
    )

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.staff_name
