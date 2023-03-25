from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField("Название категория", max_length=120)
    desciptions = models.CharField("Описание категория", max_length=250)
    titleseo = models.CharField("Titl", max_length=80)
    desciptionsseo = models.CharField("Descriptions", max_length=150)
    slug = models.SlugField(unique=True, null=True)
    img = models.ImageField("Изображение", null=True)
    icons = models.ImageField("Иконка", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categoryblog_detail', kwargs={'blogcategory_slug': self.slug})

    class Meta:
        verbose_name = "Категория поста"
        verbose_name_plural = "Категории поста"


class BlogPost(models.Model):
    name = models.CharField("Название статьи", max_length=120)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Категория поста", related_name='postsblog', null=True)
    desciptions = models.CharField("Описание статьи", max_length=250)
    text = RichTextField("Содержимое статьи")
    date = models.DateTimeField("Дата")
    titleseo = models.CharField("Titlw", max_length=80)
    desciptionsseo = models.CharField("Descriptions", max_length=150)
    slug = models.SlugField(unique=True, null=True)
    img = models.ImageField("Изображение", null=True)
    icons = models.ImageField("Иконка", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('postblog_detail', kwargs={'blogcategory_slug': self.category.slug, 'postblog_slug': self.slug})

    class Meta:
        verbose_name = "Посты в блоге"
        verbose_name_plural = "Посты в блоге"