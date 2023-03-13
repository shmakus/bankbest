# Generated by Django 4.1.5 on 2023-01-08 15:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_bank_remove_post_categorypost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='img/post_img/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoryPost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.debetcard', verbose_name='Debetcard'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение отзыва')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.reviews', verbose_name='Родитель')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post', verbose_name='Пост карточки')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('post', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='core.post', verbose_name='фильмы')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]