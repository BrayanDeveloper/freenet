# Generated by Django 2.2 on 2019-05-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_pages', '0020_auto_20190502_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas',
            name='image_caracteristica',
            field=models.ImageField(upload_to='static/img/images_counter/'),
        ),
    ]
