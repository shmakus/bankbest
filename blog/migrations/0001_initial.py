# Generated by Django 3.2.18 on 2023-03-25 18:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название категория')),
                ('desciptions', models.CharField(max_length=250, verbose_name='Описание категория')),
                ('titleseo', models.CharField(max_length=80, verbose_name='Titl')),
                ('desciptionsseo', models.CharField(max_length=150, verbose_name='Descriptions')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('icons', models.ImageField(null=True, upload_to='', verbose_name='Иконка')),
            ],
            options={
                'verbose_name': 'Категория поста',
                'verbose_name_plural': 'Категории поста',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название статьи')),
                ('desciptions', models.CharField(max_length=250, verbose_name='Описание статьи')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Содержимое статьи')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('titleseo', models.CharField(max_length=80, verbose_name='Titlw')),
                ('desciptionsseo', models.CharField(max_length=150, verbose_name='Descriptions')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('icons', models.ImageField(null=True, upload_to='', verbose_name='Иконка')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postsblog', to='blog.blogcategory', verbose_name='Категория поста')),
            ],
            options={
                'verbose_name': 'Посты в блоге',
                'verbose_name_plural': 'Посты в блоге',
            },
        ),
    ]
