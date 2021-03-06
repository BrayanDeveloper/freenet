from django.db import models


# Create your models here.
image_repeat = (('repeat','repeat'), ('no repeat','no repeat'))
class Personalization_page(models.Model):
    favicon = models.ImageField(upload_to='static/img/favicon/')
    #background_image = models.ImageField(upload_to='static/img/images_personalization/')
    background_repeat = models.CharField(choices=image_repeat, max_length=30)
    background_color = models.CharField(max_length=90)
    background_color_bar_customers = models.CharField(max_length=90)
    background_color_bar_team_redes = models.CharField(max_length=90)

    description_service = models.TextField(max_length=9000)
    font_family_description_service = models.CharField(max_length=900)
    font_size_description_service = models.CharField(max_length=900)
    color_text_description_service = models.CharField(max_length=900)
    background_color_description_service = models.CharField(max_length=900)
    border_description_service = models.CharField(max_length=900)
    border_radius_description_service = models.CharField(max_length=900)
    text_aling_description_service = models.CharField(max_length=900)

    
    
    title_service = models.CharField(max_length=900)
    font_family_service = models.CharField(max_length=900)
    font_size_service = models.CharField(max_length=900)
    color_text_service = models.CharField(max_length=900)
    background_color_service = models.CharField(max_length=900)
    border_service = models.CharField(max_length=900)
    border_radius_service = models.CharField(max_length=900)





    title_1 = models.CharField(max_length=90)
    description_area_services_professional = models.TextField(max_length=9000)
    description_area_background_color = models.CharField(max_length=90)
    description_area_color_text = models.CharField(max_length=90)
    description_area_padding = models.CharField(max_length=90)
    description_area_border = models.CharField(max_length=90)
    description_area_border_radius = models.CharField(max_length=90)
    description_area_font_size = models.CharField(max_length=90)
    description_area_font_family = models.CharField(max_length=90)
    description_area_text_aling = models.CharField(max_length=90)
    description_area_width = models.CharField(max_length=90)
    description_area_height = models.CharField(max_length=90)

    description_team = models.TextField(max_length=9000)
    description_team_background_color = models.CharField(max_length=90)
    description_team_color_text = models.CharField(max_length=90)
    description_team_padding = models.CharField(max_length=90)
    description_team_border = models.CharField(max_length=90)
    description_team_border_radius = models.CharField(max_length=90)
    description_team_font_size = models.CharField(max_length=90)
    description_team_font_family = models.CharField(max_length=90)
    description_team_text_aling = models.CharField(max_length=90)
    description_team_width = models.CharField(max_length=90)
    description_team_height = models.CharField(max_length=90)
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
    text_contact = models.CharField(max_length=900)
    text_color_contact = models.CharField(max_length=900)
    background_color_contact = models.CharField(max_length=900)
    font_family_contact = models.CharField(max_length=900)
    font_size_contact = models.CharField(max_length=900)
    border_contact = models.CharField(max_length=900)
    border_radius_contact = models.CharField(max_length=900)
    link_mape_contact = models.CharField(max_length=9000)


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
  


