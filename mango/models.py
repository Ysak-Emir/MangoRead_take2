from django.db import models

from users.models import User


class Type(models.Model):
    # id = models.AutoField()
    type = models.CharField(max_length=100, blank=False, verbose_name="Тип")

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.type


class Genre(models.Model):
    # id = models.AutoField()
    genre = models.CharField(max_length=100, blank=False, verbose_name="Жанр")


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre


class MangoCard(models.Model):
    profile_picture = models.ImageField(upload_to="mango_data/profile_picture", null=True, blank=False,
                                        verbose_name="Картинка")
    title = models.CharField(max_length=100, blank=False, verbose_name="Название манги")
    year = models.IntegerField(blank=False, verbose_name="Год")
    description = models.TextField(null=True, blank=False, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", related_name='card')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип", related_name='card')
    is_puplished = models.BooleanField(default=True, verbose_name="Публикация")

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
        ordering = ['title', 'time_create']

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=False, verbose_name="Текст")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    mango = models.ForeignKey(MangoCard, on_delete=models.CASCADE, verbose_name="Манго")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['time_create', 'user']

    def __str__(self):
        return str(self.user)


