# Generated by Django 4.1.5 on 2023-03-12 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_maincategory_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='maincategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.maincategory', verbose_name='Основная категория'),
        ),
    ]
