from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings

# Create your models here.

class BlogCategory:
    name = models.CharField("Название категория", max_length=120)
    desciptions = models.CharField("Описание категория", max_length=250)
    titleseo = models.CharField("Titlw", max_length=80)
    desciptionsseo = models.CharField("Descriptions", max_length=150)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'blogcategory_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class BlogPost:
    name = models.CharField("Название статьи", max_length=120)
    desciptions = models.CharField("Описание статьи", max_length=250)
    text = models.TextField("Содержимое статьи")
    date = models.DateTimeField("Дата")
    titleseo = models.CharField("Titlw", max_length=80)
    desciptionsseo = models.CharField("Descriptions", max_length=150)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"