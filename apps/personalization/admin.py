from django.contrib import admin
from apps.personalization.models import Personalization_page, Menu
# Register your models here.

class Personalization_page_dsplay(admin.ModelAdmin):
    list_display = ['background_color',]
    
class Menu_dsplay(admin.ModelAdmin):
    list_display = ['item1','item2','item3','item4','item5']
    

admin.site.register(Personalization_page, Personalization_page_dsplay)
admin.site.register(Menu, Menu_dsplay)