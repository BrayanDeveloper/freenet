# Generated by Django 2.2 on 2019-04-30 17:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_pages', '0016_auto_20190429_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter_page',
            name='seccion4_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
