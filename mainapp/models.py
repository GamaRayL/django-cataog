from django.db import models
from django.utils import timezone

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


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.CharField(max_length=255, unique=True, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    img_preview = models.ImageField(upload_to='blog_post_preview/', verbose_name='превью изображения')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')
    view_count = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.body} {self.create_date} {self.view_count}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('title',)
