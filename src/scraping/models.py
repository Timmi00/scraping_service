from django.db import models
from pytils.translit import slugify


class Film(models.Model):
    # url = models.URLField(
    #     unique=True
    # )
    film_name = models.CharField(
        max_length=48,
        verbose_name='Название фильма'
    )
    film_id = models.IntegerField(
        verbose_name='id фильма на кинопоиске',
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    stuffs = models.ForeignKey(
        'Staff',
        on_delete=models.CASCADE,
        default=None
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.film_name)
        super().save(*args, **kwargs)


class Staff(models.Model):
    staff_role = models.ManyToManyField(
        'Profession',
        default=None
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
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.staff_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.staff_name)
        super().save(*args, **kwargs)


class Profession(models.Model):
    profession = models.CharField(
        max_length=48
    )

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.profession
