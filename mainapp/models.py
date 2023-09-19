from django.db import models
from django.utils import timezone
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=255, verbose_name='описание')
    image_preview = models.ImageField(upload_to='preview/', verbose_name='превью изображений', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    create_at = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return (f'{self.name} {self.description} {self.image_preview} '
                f'{self.category} {self.price} {self.create_at} {self.updated_at}')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.CharField(max_length=255, unique=True, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    img_preview = models.ImageField(upload_to='post_preview/', verbose_name='превью изображения', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.body} {self.create_date} {self.view_count}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('title',)
