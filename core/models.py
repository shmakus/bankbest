from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from meta.models import ModelMeta
from ckeditor.fields import RichTextField
from meta.views import Meta
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class MainCategory(models.Model):
    name = models.CharField("Основная категория", max_length=120)
    description = models.TextField("Описание")
    slug = models.SlugField(unique=True, null=True)
    icon = models.ImageField("Иконка", null=True)
    title = models.CharField("Seo Title", max_length=80, null=True)
    descriptions = models.CharField("Seo Description", max_length=160, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('maincategory_detail', kwargs={'maincategory_slug': self.slug})

    class Meta:
        verbose_name = "Основная Категория"
        verbose_name_plural = "Основная Категории"


class Category(models.Model):
    name = models.CharField("Категория", max_length=120)
    maincategory = models.ForeignKey(MainCategory, verbose_name="Основная", on_delete=models.CASCADE, related_name='cate', null=True)
    description = models.TextField("Описание")
    slug = models.SlugField(unique=True, null=True)
    icon = models.ImageField("Иконка", null=True)
    title = models.CharField("Seo Title", max_length=80, null=True)
    descriptions = models.CharField("Seo Description", max_length=160, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'maincategory_slug': self.maincategory.slug, 'category_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class SubCategory(models.Model):
    name = models.CharField("Под категория ", max_length=120)
    description = models.TextField("Описание")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name='subcategories', null=True)
    slug = models.SlugField(unique=True, null=True)
    icon = models.ImageField("Иконка", null=True)
    title = models.CharField("Seo Title", max_length=80, null=True)
    descriptions = models.CharField("Seo Description", max_length=160, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory_detail', kwargs={'category_slug': self.category.slug, 'subcategory_slug': self.slug})

    class Meta:
        verbose_name = "Под Категория"
        verbose_name_plural = "Под Категории"


class Bank(models.Model):
    name = models.CharField("Банк", max_length=120)
    description = models.TextField("Описание банка")
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField("Seo Title", max_length=80, null=True)
    descriptions = models.CharField("Seo Description", max_length=160, null=True)
    mini_icons = models.ImageField("Иконка", null=True)
    img = models.ImageField("Изображение", null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    url_off_site = models.CharField("Офф сайт", max_length=120, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Банк"
        verbose_name_plural = "Банки"

    def get_absolute_url(self):
        return reverse('bank_detail', kwargs={'bank_slug': self.slug})


class Post(ModelMeta, models.Model):
    name = models.CharField("Пост", max_length=120)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name="Основная категория", related_name='maincate', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name='posts', null=True)
    subcategories = models.ManyToManyField(SubCategory, related_name='posts')
    description = models.TextField("Описание")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="Банк", related_name='posts', null=True)
    otziv = models.TextField("Отзывы")
    slug = models.SlugField(unique=True, null=True)
    link = models.TextField(verbose_name="Ссылка на партнерку", null=True)
    titleSeo = models.CharField("Title сео", max_length=80, null=True)
    descriptionSeo = models.CharField("Description Seo", max_length=160, null=True)
    img = models.ImageField("Изображение", null=True)
    mini_icons = models.ImageField("Иконка", null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    text = RichTextField("Text", null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'category_slug': self.category.slug, 'post_slug': self.slug})


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating (models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="фильмы")

    def __str__(self):
        return f"{self.star} - {self.post}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect, empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение отзыва", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name="Пост карточки", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



