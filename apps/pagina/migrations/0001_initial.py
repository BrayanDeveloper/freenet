# Generated by Django 2.1.7 on 2019-04-15 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=40)),
                ('description_service', models.CharField(max_length=100)),
                ('image_service', models.ImageField(upload_to='static/images_services/')),
                ('link_service', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service_plus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=40)),
                ('description_service', models.CharField(max_length=100)),
                ('image_service', models.ImageField(upload_to='static/images_services/')),
                ('link_service', models.CharField(max_length=255)),
                ('price_service', models.CharField(max_length=255)),
                ('developer_service', models.CharField(max_length=255)),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.Service')),
            ],
        ),
    ]
