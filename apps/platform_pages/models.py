from django.db import models

# Create your models here.
class Counter_page(models.Model):
    favicon = models.ImageField(upload_to='static/img/favicon/')
    #background_image = models.ImageField(upload_to='static/img/images_personalization/')
    logo = models.ImageField(upload_to='static/img/logo/')
    font_family_titles = models.CharField(max_length=90)
    font_sizes_titles = models.CharField(max_length=90)
    background_color_titles = models.CharField(max_length=90)    
    color_titles = models.CharField(max_length=90)
    width_titles = models.CharField(max_length=90)
    height_titles = models.CharField(max_length=90)
    border_titles = models.CharField(max_length=90)
    border_radius_titles = models.CharField(max_length=90)
    font_family_paragrafos = models.CharField(max_length=90)
    font_sizes_paragrafos = models.CharField(max_length=90)
    background_color_paragrafos = models.CharField(max_length=90)    
    color_paragrafos = models.CharField(max_length=90)
    width_paragrafos = models.CharField(max_length=90)
    height_paragrafos = models.CharField(max_length=90)
    border_paragrafos = models.CharField(max_length=90)
    border_radius_paragrafos = models.CharField(max_length=90)
    


    title1 = models.CharField(max_length=90)
    image_title1 = models.ImageField(upload_to='static/img/images_counter/')
    description_title1 = models.CharField(max_length=9000)

    seccion1_title = models.CharField(max_length=90)
    image_seccion1 = models.ImageField(upload_to='static/img/images_counter/')
    description_seccion1 = models.CharField(max_length=9000)
    width_image_seccion1 = models.CharField(max_length=90)
    height_image_seccion1 = models.CharField(max_length=90)
    padding_image_seccion1 = models.CharField(max_length=90)
    border_image_seccion1 = models.CharField(max_length=90)
    border_radius_image_seccion1 = models.CharField(max_length=90)  
    


    caracteristicas_title = models.CharField(max_length=90)
    description_caracteristicas = models.CharField(max_length=9000)

    planes_title = models.CharField(max_length=90)
    description_planes = models.CharField(max_length=9000)

    def __str__(self):
        return 'id page: ' + self.title1


class Caracterist(models.Model):
    caracteristicas_title = models.CharField(max_length=90)
    description_caracteristicas = models.CharField(max_length=9000)
    image_caracteristica = models.ImageField(upload_to='static/img/images_counter/')
    background_color_caracteristica = models.CharField(max_length=90)
    padding_caracteristica = models.CharField(max_length=90)
    border_caracteristica = models.CharField(max_length=90)
    border_radius_caracteristica = models.CharField(max_length=90)
    id_counter_page = models.ForeignKey(Counter_page, on_delete=models.CASCADE)



