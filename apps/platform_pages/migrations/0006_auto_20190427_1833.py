# Generated by Django 2.2 on 2019-04-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_pages', '0005_auto_20190427_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristicas',
            name='border_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='border_radius_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='height_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='width_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='border_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='border_radius_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='height_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='width_image',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
