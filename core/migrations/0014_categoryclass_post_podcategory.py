# Generated by Django 4.1.5 on 2023-03-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Под категория категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, null=True, unique=True)),
                ('icon', models.ImageField(null=True, upload_to='', verbose_name='Иконка')),
                ('categoryPost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category', verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='podcategory',
            field=models.ManyToManyField(null=True, to='core.categoryclass', verbose_name='Подкатегория'),
        ),
    ]