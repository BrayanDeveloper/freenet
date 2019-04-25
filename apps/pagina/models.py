from django.db import models

# Create your models here.


class Service(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=6000)
    color_background = models.CharField(max_length=60)
    border = models.CharField(max_length=60)
    border_radius = models.CharField(max_length=60)
    color_text = models.CharField(max_length=60)
    font_size = models.CharField(max_length=60)
    text_transform = models.CharField(max_length=60)
    font_family = models.CharField(max_length=60)
    padding = models.CharField(max_length=60)
    image_service = models.ImageField(upload_to='static/img/images_services/')
    width_image = models.CharField(max_length=60)
    height_image = models.CharField(max_length=60)
    link_service = models.CharField(max_length=255)
    def __str__(self):
        return 'id servicio: ' + self.name_service


class Service_plus(models.Model):
    name_service = models.CharField(max_length=500)
    description_service = models.CharField(max_length=9000)
    color_background = models.CharField(max_length=60)
    image_service = models.ImageField(upload_to='static/img/images_services/')
    image_width = models.CharField(max_length=60)
    image_height = models.CharField(max_length=60)
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
    width_image = models.CharField(max_length=100)
    height_image = models.CharField(max_length=100)

class Ask_frecuent(models.Model):
    ask = models.CharField(max_length=600)
    answer = models.CharField(max_length=600)
    image = models.ImageField(upload_to='static/img/images_ask_frecuent/')

class Slider_setting(models.Model):
    title = models.CharField(max_length=600)
    horizontal_text_shadow = models.CharField(max_length=600)
    vertical_text_shadow = models.CharField(max_length=600)
    blur_radius_text_shadow = models.CharField(max_length=600)
    color_text_shadow = models.CharField(max_length=600)
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
    width_image = models.CharField(max_length=90)
    height_image = models.CharField(max_length=90)
    border_radius_image = models.CharField(max_length=90)
    description = models.CharField(max_length=9000)
    edad = models.CharField(max_length=9000)
    habilidades = models.CharField(max_length=9000)
    hobbies = models.CharField(max_length=9000)
    profeccion = models.CharField(max_length=900)
    color_background = models.CharField(max_length=90)
    color_text = models.CharField(max_length=60)
    font_size = models.CharField(max_length=60)
    text_transform = models.CharField(max_length=60)
    font_family = models.CharField(max_length=60)
    padding_text = models.CharField(max_length=60)
    text_aling = models.CharField(max_length=60)
    border_radius = models.CharField(max_length=90)
    border = models.CharField(max_length=90)



class Footer(models.Model):
    phone = models.CharField(max_length=90)
    image_phone = models.ImageField(upload_to='static/img/images_footer/')
    celphone = models.CharField(max_length=90)
    image_celphone = models.ImageField(upload_to='static/img/images_footer/')
    email = models.CharField(max_length=90)
    image_email = models.ImageField(upload_to='static/img/images_footer/')
    address = models.CharField(max_length=200)
    image_address = models.ImageField(upload_to='static/img/images_footer/')
    city = models.CharField(max_length=90)
    image_city = models.ImageField(upload_to='static/img/images_footer/')
    country = models.CharField(max_length=90)
    color_text = models.CharField(max_length=90)
    font_text = models.CharField(max_length=90)
    font_size = models.CharField(max_length=90)
    image_country = models.ImageField(upload_to='static/img/images_footer/')
    page_main = models.CharField(max_length=90)
    image_page = models.ImageField(upload_to='static/img/images_footer/')
    copy = models.CharField(max_length=90)
    font_family_footer = models.CharField(max_length=90)
    width_icon_copy = models.CharField(max_length=90)
    height_icon_copy = models.CharField(max_length=90)
    font_size_footer = models.CharField(max_length=90)
    padding_icon_copy = models.CharField(max_length=90)
    image_copy = models.ImageField(upload_to='static/img/images_footer/')
    background_color_copy = models.CharField(max_length=90)
    padding_copy = models.CharField(max_length=90)
    slogan = models.CharField(max_length=200)
    schedule = models.CharField(max_length=200)
    image_schedule = models.ImageField(upload_to='static/img/images_footer/')
    color_background = models.CharField(max_length=90)
    icon_facebook = models.ImageField(upload_to='static/img/images_social/')
    url_facebook = models.CharField(max_length=900)
    icon_whatsapp = models.ImageField(upload_to='static/img/images_social/')
    url_whatsapp = models.CharField(max_length=900)
    icon_instagram = models.ImageField(upload_to='static/img/images_social/')
    url_instagram = models.CharField(max_length=900)
    icon_youtube = models.ImageField(upload_to='static/img/images_social/')
    url_youtube = models.CharField(max_length=900)


class Customer(models.Model):
    name = models.CharField(max_length=40)
    image_customer = models.ImageField(upload_to='static/img/images_customers/')
    with_image = models.CharField(max_length=100)
    height_image = models.CharField(max_length=100)
    border = models.CharField(max_length=100)
    border_radius_image = models.CharField(max_length=100)
    padding_image = models.CharField(max_length=100)
    margin_image = models.CharField(max_length=100)
    description = models.CharField(max_length=9000)
    email = models.CharField(max_length=100)
    cel_phone = models.CharField(max_length=12)

