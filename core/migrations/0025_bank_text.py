# Generated by Django 3.2.18 on 2023-03-26 05:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20230325_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='text',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
    ]