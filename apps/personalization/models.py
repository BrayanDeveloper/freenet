from django.db import models

# Create your models here.
image_repeat = (('repeat','repeat'), ('no repeat','no repeat'))
class Personalization_page(models.Model):
    #background_image = models.ImageField(upload_to='static/img/images_personalization/')
    background_repeat = models.CharField(choices=image_repeat, max_length=30)
    background_color = models.CharField(max_length=90)
    background_color_bar_customers = models.CharField(max_length=90)
    title_1 = models.CharField(max_length=90)
    title_2 = models.CharField(max_length=90)
    title_3 = models.CharField(max_length=90)
    title_4 = models.CharField(max_length=90)
    font_family_title = models.CharField(max_length=90)
    color_text = models.CharField(max_length=90)
    text_aling = models.CharField(max_length=90)
    float_text = models.CharField(max_length=90)
    text_transform = models.CharField(max_length=90)
    border = models.CharField(max_length=90) 
    padding_text = models.CharField(max_length=90)
    border_radius = models.CharField(max_length=90)



class Menu(models.Model):
    color_background = models.CharField(max_length=30)
    color_text_menu = models.CharField(max_length=30)
    color_background_submenu = models.CharField(max_length=30)
    color_text_submenu = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='static/img/logo/')
    width_image = models.CharField(max_length=30)
    item1 = models.CharField(max_length=30)
    item2 = models.CharField(max_length=30)
    item3 = models.CharField(max_length=30)
    item4 = models.CharField(max_length=30)
    item5 = models.CharField(max_length=30)
    item6 = models.CharField(max_length=30)
    background_color_item6 = models.CharField(max_length=30)
    background_color_item6_hover = models.CharField(max_length=30)
  


