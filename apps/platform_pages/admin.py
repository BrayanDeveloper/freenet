from django.contrib import admin
from apps.platform_pages.models import Counter_page, Caracteristicas, Plan, Publicidad_page, servicios_publicidad_page
# Register your models here.
class DisplayCounterPage(admin.ModelAdmin):
    list_display = ['title1',]

class DisplayCaracteristicas(admin.ModelAdmin):
    list_display = ['caracteristicas_title',]

class DisplayPlanes(admin.ModelAdmin):
    list_display = ['plan_title',]

class DisplayPublicidad_page(admin.ModelAdmin):
    list_display = ['title_pestana',]

class DisplaySevices_Publicidad_page(admin.ModelAdmin):
    list_display = ['name_service','description_service']

admin.site.register(Counter_page, DisplayCounterPage)
admin.site.register(Caracteristicas, DisplayCaracteristicas)
admin.site.register(Plan, DisplayPlanes)

admin.site.register(Publicidad_page, DisplayPublicidad_page)
admin.site.register(servicios_publicidad_page, DisplaySevices_Publicidad_page)
