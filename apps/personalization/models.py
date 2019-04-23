from django.db import models

# Create your models here.
image_repeat = (('repeat','repeat'), ('no repeat','no repeat'))
class Personalization_page(models.Model):
    #background_image = models.ImageField(upload_to='static/img/images_personalization/')
    background_repeat = models.CharField(choices=image_repeat, max_length=30)
    background_color = models.CharField(max_length=90)

class Menu(models.Model):
    logo = models.ImageField(upload_to='static/img/logo/')
    item1 = models.CharField(max_length=30)
    item2 = models.CharField(max_length=30)
    item3 = models.CharField(max_length=30)
    item4 = models.CharField(max_length=30)
    item5 = models.CharField(max_length=30)
  


