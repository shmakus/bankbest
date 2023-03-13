# Generated by Django 4.1.5 on 2023-01-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Банк')),
                ('description', models.TextField(verbose_name='Описание банка')),
                ('url', models.SlugField(max_length=160, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Основная категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Пост')),
                ('description', models.TextField(verbose_name='Описание')),
                ('otziv', models.TextField(verbose_name='otzivi')),
                ('rating', models.TextField(verbose_name='rating')),
                ('url', models.SlugField(max_length=160, null=True, unique=True)),
                ('bank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.bank')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
    ]