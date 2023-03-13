# Generated by Django 4.1.5 on 2023-03-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_rename_slug_bank_url_rename_slug_category_url_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryClass',
            new_name='SubCategory',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categoryPost',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='categoryPost',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='podcategory',
        ),
        migrations.AddField(
            model_name='post',
            name='subcategories',
            field=models.ManyToManyField(related_name='posts', to='core.subcategory'),
        ),
    ]
