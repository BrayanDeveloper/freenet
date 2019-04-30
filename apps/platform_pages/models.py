from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Counter_page(models.Model):
    favicon = models.ImageField(upload_to='static/img/favicon/')
    title_pestana = models.CharField(max_length=90)
    logo = models.ImageField(upload_to='static/img/logo/')
    width_logo = models.CharField(max_length=90)
    background_color_page = models.CharField(max_length=90)
    font_family_titles = models.CharField(max_length=90)
    font_sizes_titles = models.CharField(max_length=90)
    background_color_titles = models.CharField(max_length=90)
    color_titles = models.CharField(max_length=90)
    width_titles = models.CharField(max_length=90)
    height_titles = models.CharField(max_length=90)
    padding_titles = models.CharField(max_length=90)
    text_aling_titles = models.CharField(max_length=90)
    border_titles = models.CharField(max_length=90)
    border_radius_titles = models.CharField(max_length=90)
    font_family_paragrafos = models.CharField(max_length=90)
    font_sizes_paragrafos = models.CharField(max_length=90)
    background_color_paragrafos = models.CharField(max_length=90)
    color_paragrafos = models.CharField(max_length=90)
    width_paragrafos = models.CharField(max_length=90)
    text_aling_paragrafos = models.CharField(max_length=90)
    height_paragrafos = models.CharField(max_length=90)
    border_paragrafos = models.CharField(max_length=90)
    border_radius_paragrafos = models.CharField(max_length=90)



    title1 = models.CharField(max_length=90)
    color_title1 = models.CharField(max_length=90)
    background_color_title1 = models.CharField(max_length=90)
    border_radius_title1 = models.CharField(max_length=90)
    horizontal_text_shadow = models.CharField(max_length=90)
    vertical_text_shadow = models.CharField(max_length=90)
    blur_text_shadow = models.CharField(max_length=90)
    color_text_shadow = models.CharField(max_length=90)
    image_title1 = models.ImageField(upload_to='static/img/images_counter/')
    background_color_image = models.ImageField(upload_to='static/img/images_counter/')
    background_repeat = models.ImageField(upload_to='static/img/images_counter/')
    description1 = models.CharField(max_length=9000)
    color_descripcion1 = models.CharField(max_length=90)

    seccion2_title = models.CharField(max_length=90)
    image_seccion2 = models.ImageField(upload_to='static/img/images_counter/')
    description_seccion2 = models.CharField(max_length=9000)
    width_image_seccion2 = models.CharField(max_length=90)
    height_image_seccion2 = models.CharField(max_length=90)
    padding_image_seccion2 = models.CharField(max_length=90)
    border_image_seccion2 = models.CharField(max_length=90)
    border_radius_image_seccion2 = models.CharField(max_length=90)



    seccion3_title = models.CharField(max_length=90)
    seccion3_description = models.CharField(max_length=9000)

    seccion4_title = models.CharField(max_length=90)
    seccion4_description = RichTextField(blank=True, null=True)

    for_page = models.CharField(max_length=30)

    def __str__(self):
        return 'id page: ' + self.title1


class Caracteristicas(models.Model):
    caracteristicas_title = models.CharField(max_length=90)
    description_caracteristicas = models.CharField(max_length=9000)
    image_caracteristica = models.ImageField(upload_to='static/img/images_counter/')
    background_color_caracteristica = models.CharField(max_length=90)
    font_family = models.CharField(max_length=90)
    font_size = models.CharField(max_length=90)
    padding_caracteristica = models.CharField(max_length=90)
    border_caracteristica = models.CharField(max_length=90)
    border_radius_caracteristica = models.CharField(max_length=90)
    width_image = models.CharField(max_length=90)
    height_image = models.CharField(max_length=90)
    border_image = models.CharField(max_length=90)
    border_radius_image = models.CharField(max_length=90)
    background_color_contenedor = models.CharField(max_length=90)
    height_contenedor = models.CharField(max_length=90)
    id_counter_page = models.ForeignKey(Counter_page, on_delete=models.CASCADE)


class Plan(models.Model):
    plan_title = RichTextField(blank=True, null=True)
    icono_plan = models.ImageField(upload_to='static/img/images_counter/')
    width_icon = models.CharField(max_length=9000)
    height_icon = models.CharField(max_length=9000)
    padding_icon = models.CharField(max_length=9000)
    
    description_plan = RichTextField(blank=True, null=True)
    text_aling_description = models.CharField(max_length=9000)
    padding_text_description = models.CharField(max_length=9000)
    color_background_caja_texto = models.CharField(max_length=90)
    color_background_caja_description = models.CharField(max_length=90)
    price_plan = RichTextField(blank=True, null=True)
    background_color_contenedor = models.CharField(max_length=90)
    height_contenedor = models.CharField(max_length=90)
    id_counter_page = models.ForeignKey(Counter_page, on_delete=models.CASCADE)


class Publicidad_page(models.Model):
    favicon = models.ImageField(upload_to='static/img/favicon/')
    title_pestana = models.CharField(max_length=90)
    #background_image = models.ImageField(upload_to='static/img/images_personalization/')
    logo = models.ImageField(upload_to='static/img/logo/')
    width_logo = models.CharField(max_length=90)
    background_color_page = models.CharField(max_length=90)
    font_family_titles = models.CharField(max_length=90)
    font_sizes_titles = models.CharField(max_length=90)
    background_color_titles = models.CharField(max_length=90)
    color_titles = models.CharField(max_length=90)
    width_titles = models.CharField(max_length=90)
    height_titles = models.CharField(max_length=90)
    padding_titles = models.CharField(max_length=90)
    text_aling_titles = models.CharField(max_length=90)
    border_titles = models.CharField(max_length=90)
    border_radius_titles = models.CharField(max_length=90)
    font_family_paragrafos = models.CharField(max_length=90)
    font_sizes_paragrafos = models.CharField(max_length=90)
    background_color_paragrafos = models.CharField(max_length=90)
    color_paragrafos = models.CharField(max_length=90)
    width_paragrafos = models.CharField(max_length=90)
    text_aling_paragrafos = models.CharField(max_length=90)
    height_paragrafos = models.CharField(max_length=90)
    border_paragrafos = models.CharField(max_length=90)
    border_radius_paragrafos = models.CharField(max_length=90)



    title1 = models.CharField(max_length=90)
    color_title1 = models.CharField(max_length=90)
    background_color_title1 = models.CharField(max_length=90)
    border_radius_title1 = models.CharField(max_length=90)
    horizontal_text_shadow = models.CharField(max_length=90)
    vertical_text_shadow = models.CharField(max_length=90)
    blur_text_shadow = models.CharField(max_length=90)
    color_text_shadow = models.CharField(max_length=90)
    image_title1 = models.ImageField(upload_to='static/img/images_counter/')
    background_color_image = models.ImageField(upload_to='static/img/images_counter/')
    background_repeat = models.ImageField(upload_to='static/img/images_counter/')
    description1 = models.CharField(max_length=9000)
    color_descripcion1 = models.CharField(max_length=90)

    seccion2_title = models.CharField(max_length=90)
    image_seccion2 = models.ImageField(upload_to='static/img/images_counter/')
    description_seccion2 = models.CharField(max_length=9000)
    width_image_seccion2 = models.CharField(max_length=90)
    height_image_seccion2 = models.CharField(max_length=90)
    padding_image_seccion2 = models.CharField(max_length=90)
    border_image_seccion2 = models.CharField(max_length=90)
    border_radius_image_seccion2 = models.CharField(max_length=90)



    seccion3_title = models.CharField(max_length=90)
    seccion3_description = models.CharField(max_length=9000)

    seccion4_title = models.CharField(max_length=90)
    seccion4_description = models.CharField(max_length=9000)

    for_page = models.CharField(max_length=30)

    def __str__(self):
        return 'id page: ' + self.title1
