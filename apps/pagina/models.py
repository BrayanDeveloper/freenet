from django.db import models

# Create your models here.


class Service(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=6000)
    color_background = models.CharField(max_length=60)
    image_service = models.ImageField(upload_to='static/img/images_services/')
    link_service = models.CharField(max_length=255)
    def __str__(self):
        return 'id servicio: ' + self.name_service


class Service_plus(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=9000)
    image_service = models.ImageField(upload_to='static/img/images_services/')
    link_service = models.CharField(max_length=255)
    price_service = models.CharField(max_length=255)
    developer_service = models.CharField(max_length=255)
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=40)
    message = models.CharField(max_length=9000)
    email = models.CharField(max_length=100)

class Appointment(models.Model):
    name = models.CharField(max_length=40)
    message = models.CharField(max_length=9000)
    email = models.CharField(max_length=100)
    cel_phone = models.CharField(max_length=12)
    dia = models.DateField()

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=9000)
    image = models.ImageField(upload_to='static/img/images_about/')

class Ask_frecuent(models.Model):
    ask = models.CharField(max_length=600)
    answer = models.CharField(max_length=600)
    image = models.ImageField(upload_to='static/img/images_ask_frecuent/')

class Personalization(models.Model):
    title = models.CharField(max_length=600)
    color_title = models.CharField(max_length=20)
    description = models.CharField(max_length=9000)
    color_description = models.CharField(max_length=20)
    font_type = models.CharField(max_length=20)
    font_size = models.CharField(max_length=20)
    background_color_text = models.CharField(max_length=20)
    border_radius_background = models.CharField(max_length=20)
    image_transition = models.ImageField(upload_to='static/img/images_personalization/')
    image_fondo = models.ImageField(upload_to='static/img/images_personalization/')
    link = models.CharField(max_length=600)

class Team(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='static/img/images_team_freenet/')
    description = models.CharField(max_length=9000)
    profeccion = models.CharField(max_length=900)





