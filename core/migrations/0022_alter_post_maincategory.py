# Generated by Django 4.1.5 on 2023-03-12 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_post_maincategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='maincategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincate', to='core.maincategory', verbose_name='Основная категория'),
        ),
    ]
