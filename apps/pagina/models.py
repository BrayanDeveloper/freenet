from django.db import models

# Create your models here.


class Service(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=6000)
    image_service = models.ImageField(upload_to='staticfiles/img/images_services/')
    link_service = models.CharField(max_length=255)
    def __str__(self):
        return 'id servicio: ' + self.name_service


class Service_plus(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=9000)
    image_service = models.ImageField(upload_to='staticfiles/img/images_services/')
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
    image = models.ImageField(upload_to='staticfiles/img/images_about/')




