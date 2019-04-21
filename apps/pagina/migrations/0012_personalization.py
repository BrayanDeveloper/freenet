# Generated by Django 2.2 on 2019-04-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_auto_20190419_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personalization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
                ('description', models.CharField(max_length=9000)),
                ('image', models.ImageField(upload_to='static/img/images_personalization/')),
                ('link', models.CharField(max_length=600)),
            ],
        ),
    ]
